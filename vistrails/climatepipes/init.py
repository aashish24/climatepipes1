import os, sys
import shutil
import urllib
import uuid

from core.modules.vistrails_module import Module, ModuleError
from core.modules.basic_modules import Constant, File, String, Integer, List, \
    PythonSource
import core.modules.module_registry

from identifiers import *
import vcs_util
from convert import *

sys.path.append(os.path.dirname(__file__))
import esgf_utils

web_server_path = os.path.join( \
    os.environ.get("CATALINA_HOME",
                   "/home/aashish/tools/paraviewweb/tomcat/apache-tomcat-6.0.35"),
    "webapps")
web_out_dir = 'Climate/tmp'

##############################################################################

class WebSink(Module):
    _input_ports = [("value", "(edu.utah.sci.vistrails.basic:Module)"),
                    ("contentType", "(edu.utah.sci.vistrails.basic:String)")]

    def compute(self):
        value = self.getInputFromPort("value")
        contentType = self.forceGetInputFromPort("contentType", None)
        if isinstance(value, File):
            suffix = os.path.splitext(value.name)[1]
            if contentType is None and suffix:
                if suffix[1:] == 'png':
                    contentType = 'image/png'
                elif suffix[1:] == 'jpg' or suffix[1:] == 'jpeg':
                    contentType = 'image/jpg'
            output_fname = os.path.join(web_out_dir,
                                        'vt_%s%s' % (uuid.uuid4().hex, suffix))
            # print "**", web_server_path, web_out_dir, os.path.join(web_server_path, output_fname)
            shutil.copyfile(value.name, os.path.join(web_server_path,
                                                     output_fname))
            print 'Content-Type: %s' % contentType
            print "/%s" % output_fname,
        elif isinstance(value, Constant):
            strValue = value.translate_to_string(value)
            if contentType is None:
                contentType = 'text/plain'
            print 'Content-Type: %s' % contentType
            print strValue,
        else:
            strValue = str(value)
            if contentType is None:
                contentType = 'text/plain'
            print 'Content-Type: %s' % contentType
            print strValue,

class WebConfigSink(PythonSource):
    _input_ports = [("contentType", "(edu.utah.sci.vistrails.basic:String)")]
    def push_to_web(self, fname):
        if isinstance(fname, File):
            fname = fname.name
        if not os.path.exists(fname):
            raise ModuleError(self, "Cannot push file '%s' to the web because "
                              "it does not exist" % fname)
        suffix = os.path.splitext(fname)[1]
        output_fname = os.path.join(web_out_dir,
                                    'vt_%s%s' % (uuid.uuid4().hex, suffix))
        shutil.copyfile(fname, os.path.join(web_server_path, output_fname))
        return "/" + output_fname

    def compute(self):
        contentType = self.forceGetInputFromPort("contentType", None)
        if contentType is None:
            contentType = 'text/plain'
        print "Content-Type: %s" % contentType
        s = urllib.unquote(str(self.forceGetInputFromPort('source', '')))
        self.run_code(s, use_input=True, use_output=False)

##############################################################################

class CDMSVariable(Module):
    _input_ports = [("data", "(edu.utah.sci.vistrails.basic:File)"),
                    ("variable", "(edu.utah.sci.vistrails.basic:String)")]
    _output_ports = [("value", "(%s:CDMSVariable)" % identifier)]

    def compute(self):
        self.data_file = self.getInputFromPort("data")
        self.var_name = self.getInputFromPort("variable")
        self.var = vcs_util.get_variable(self.data_file.name, self.var_name)
        self.setResult("value", self)

class ListVariables(Module):
    _input_ports = [("data", "(edu.utah.sci.vistrails.basic:File)")]
    _output_ports = [("variables", "(edu.utah.sci.vistrails.basic:List)")]

    def compute(self):
        data = self.getInputFromPort("data")
        suffix = os.path.splitext(data.name)[1][1:]
        if suffix != "nc":
            raise ModuleError(self, "Invalid file type.  " \
                                  "Expecting '.nc' and got '.%s'" % suffix)
        variables = vcs_util.get_variable_list(data.name)
        self.setResult("variables", variables)

class vcsPlot(Module):
    _input_ports = [("variable", "(%s:CDMSVariable)" % identifier),
                    ("variable2", "(%s:CDMSVariable)" % identifier)]
    _output_ports = [("image", "(edu.utah.sci.vistrails.basic:File)")]

    def compute(self):
        variable = self.getInputFromPort("variable")
        variable2 = self.forceGetInputFromPort("variable2", None)
        if variable2 is not None:
            var2 = variable2.var
        else:
            var2 = None
        output = self.interpreter.filePool.create_file(suffix='.png')
        image = vcs_util.plot(self.plot_type, output.name, variable.var, var2)
        self.setResult("image", output)

##############################################################################

class CropImage(Module):
    _input_ports = [("image", "(edu.utah.sci.vistrails.basic:Module)")]

    _output_ports= [("image", "(edu.utah.sci.vistrails.basic:File)")]

    def compute(self):
        if self.hasInputFromPort("image"):
            image = self.getInputFromPort("image")

            if isinstance(image, File):
                suffix = os.path.splitext(image.name)[1][1:]
                if suffix != "png":
                    print "Error: \nInvalid file type. Expecting '.png' and got '.%s'" % suffix
                    return

                img = crop_whitespace(image.name)
                output = self.interpreter.filePool.create_file(suffix='.png')
                img.save(output.name, "PNG")

                self.setResult("image", output)


##############################################################################

#-------------------------------------------------------------------------Source
'''
Base class for source modules. 
Subclasses should implement query and download.
'''
class cpSource(Module):
    '''
    @query: string used to query files from the source
    returns: dictionary of data urls along with their variables and rank
    '''
    def queryFiles(self, query):
        raise NotImplementedError("query method not implemented")

    '''
    @files: dictionary returned from query
    returns: list of CDMSVariable objects after downloading the files
    '''
    def download(self, files):
        raise NotImplementedError("download method not implemented")

# ------------------------------------------------------------------------Login
class ESGFSource(cpSource):
    '''
    ESGFSource is used to login to ESGF and to download files
    '''
    def compute(self):
    # host = 'pcmdi3.llnl.gov'
    # port = 2119
    # user = 'nix'
    # password = '2PW4kw'
    # keyCertFile = '/tmp/keyCert.esgf'

        host = self.forceGetInputFromPort("host", "pcmdi3.llnl.gov")
        port = self.forceGetInputFromPort("port", 2119)
        user = self.forceGetInputFromPort("user", "nix")
        password = self.forceGetInputFromPort("password", "2pw4kw")
        keyCertFile = self.interpreter.filePool.create_file(suffix='.pem')

        result = esgf_utils.login(host, port, user, password, keyCertFile.name)
        if result != keyCertFile.name:
            keyCertFile.name = result
            keyCertFile.upToDate = True

        self._keyCertFile = keyCertFile
        self.setResult("source", self)

    def queryFiles(self, query):
        url = 'http://pcmdi9.llnl.gov'
        project = 'CMIP5'
        results = esgf_utils.fetchData(
            esgf_utils.makeESGFSearchURL(url, project, query) ,query);
        return results

    def download(self, files):
        datalist = []
        for f in files:
            tmpfile = esgf_utils.extractFileNameFromURL(f["url"])
            if(esgf_utils.httpDownloadFile(self._keyCertFile.name, f["url"], tmpfile)):
                cdms = CDMSVariable()
                cdms.data_file = File();
                cdms.data_file.name = tmpfile;
                cdms.var_name = f["var"][0]["short_name"]
                cdms.var = vcs_util.get_variable(tmpfile, cdms.var_name); 
                datalist[len(datalist):] = [cdms]
            else:
                print "Error downloading file %s" % f["url"]
        return datalist        

    _input_ports =[('host', "(edu.utah.sci.vistrails.basic:String)"),
                   ('port', "(edu.utah.sci.vistrails.basic:Integer)"),
                   ('user', "(edu.utah.sci.vistrails.basic:String)"),
                   ('password', "(edu.utah.sci.vistrails.basic:String)")]

    _output_ports = [("source", "(%s:cpSource)" % identifier)]

# -----------------------------------------------------------------------Search
class ESGFSearch(Module):
    '''
    ESGFSearch is a module that downloads metadata form ESGF.
    '''
    def compute(self):
        query = self.forceGetInputFromPort("query", None)
        url = self.forceGetInputFromPort("url","http://pcmdi9.llnl.gov")
        project = self.forceGetInputFromPort("project",'CMIP5')
        result = esgf_utils.fetchData(esgf_utils.makeESGFSearchURL(url, project, query)
                                      ,query);
        self.setResult("value", result)

    _input_ports = [('query', "(edu.utah.sci.vistrails.basic:String)", True),
                    ('url', "(edu.utah.sci.vistrails.basic:String)"),
                    ('project', "(edu.utah.sci.vistrails.basic:String)")]
    _output_ports = [('value', "(edu.utah.sci.vistrails.basic:List)")]

# ---------------------------------------------------------------------Download
class ESGFDownloadFile(Module):
    '''
    Downloads specified files from ESGF. Needs ESGF key and fileName.
    '''
    def compute(self):
        keyCertFile = self.getInputFromPort("keyCertFile")
        url = self.getInputFromPort("url")
        # fileName = self.getInputFromPort("fileName")
        # outputFile = File()
        # outputFile.name = "/tmp/dataTestFile2.nc"
        # outputFile.upToDate = True

        outputFile = esgf_utils.extractFileNameFromURL(url)
        # outputFile = self.interpreter.filePool.create_file(suffix='.nc')
        result = esgf_utils.httpDownloadFile(keyCertFile.name, url, outputFile.name)
        self.setResult("outputFile", [outputFile, "mrrso", (-90.0,90.0), (-180.0,175.0)])

    _input_ports = [('keyCertFile', "(edu.utah.sci.vistrails.basic:File)"),
                    ('url', "(edu.utah.sci.vistrails.basic:String)")]
    _output_ports = [('output', "(edu.utah.sci.vistrails.basic:List)")]

#-----------------------------------------------------------------------Query
'''
Abstract module to hide how the file is retrieved (downloaded, 
cached, from disk, etc.)
'''
class cpQuery(Module):

    ''' returns list of CDMSVariable for each queried file '''
    def getData(self):
        raise NotImplementedError("getData method not implemented")

    ''' returns list of dictionary objects describing the files '''
    def getFiles(self):
        raise NotImplementedError("getFiles method not implemented")

class Query(cpQuery):
    '''
    Finds files on a source based on query parameters
    '''
    def compute(self):
        source = self.getInputFromPort("source")
        keywords = self.forceGetInputFromPort("keywords", 'temperature')
#        datefrom = self.getInputFromPort("datefrom")
#        dateto = self.getInputFromPort("dateto")
#        location = self.getInputFromPort("location")
        numitems = self.forceGetInputFromPort("numitems", 1)

        #TODO: combine parameters to create query
        query = keywords
        
        results = source.queryFiles(query)
        results = results[0:numitems] #truncate results

        self._source = source
        self._files = results

        self.setResult('query', self)

    '''
    Downloads data from source
    '''
    def getData(self):
        return self._source.download(self._files)

    def getFiles(self):
        return self._files

    _input_ports = [('source', "(%s:cpSource)" % identifier),
                    ('Keywords', "(edu.utah.sci.vistrails.basic:String)"),
                    ('From', "(edu.utah.sci.vistrails.basic:String)"),
                    ('To', "(edu.utah.sci.vistrails.basic:String)"),
                    ('Location', "(edu.utah.sci.vistrails.basic:String)"),
                    ('numitems', "(edu.utah.sci.vistrails.basic:Integer)")]
                   

    _output_ports = [('query', "(%s:cpQuery)" % identifier)]

'''
Allows user to specify the file URL
'''
class DataFile(cpQuery):

    def compute(self):
        self._source = self.getInputFromPort("source");
        url = self.getInputFromPort("url");
        var = self.getInputFromPort("variable");

        self._files = [{"url":url,"var":[{"name":"","short_name":var,"rank":1.0}],"rank":1.0}]
        self.setResult("query",self);

    '''
    Downloads data from source
    '''
    def getData(self):
        return self._source.download(self._files)

    def getFiles(self):
        return self._files

    _input_ports = [('source', "(%s:cpSource)" % identifier),
                    ('url', "(edu.utah.sci.vistrails.basic:String)"),
                    ('variable', "(edu.utah.sci.vistrails.basic:String)")]
                   

    _output_ports = [('query', "(%s:cpQuery)" % identifier)]
        
class GetFirstQueryData(Module):
    '''
    Outputs the first CDMSVariable from the query data
    '''
    def compute(self):
        query = self.getInputFromPort('query')
        data = query.getData()
        first = data[0]
        self.setResult("value", first)

    _input_ports = [("query", "(%s:cpQuery)" % identifier)]

    _output_ports = [("value", "(%s:CDMSVariable)" % identifier)]

class QueryToJSON(Module):
    '''
    Converts the list of file dictionary objects to json string
    '''

    def compute(self):
        from json import dumps
        query = self.getInputFromPort('query')
        files = query.getFiles()
        jsonstr = dumps(files, separators=(',',':'))
        self.setResult('json', jsonstr)

    _input_ports = [('query', "(%s:cpQuery)" % identifier)]
    _output_ports = [('json', "(edu.utah.sci.vistrails.basic:String)")]

class KitwareSource(cpSource):
    '''
    KitwareSource is used to login to ESGF and to download files
    '''
    def compute(self):
        host = self.forceGetInputFromPort("host", "pcmdi3.llnl.gov")
        port = self.forceGetInputFromPort("port", 2119)
        user = self.forceGetInputFromPort("user", "nix")
        password = self.forceGetInputFromPort("password", "2pw4kw")

        # NOTE: On server just create one and use that all the time
        keyCertFile = self.interpreter.filePool.create_file(suffix='.pem')

        result = esgf_utils.login(host, port, user, password, keyCertFile.name)
        if result != keyCertFile.name:
            keyCertFile.name = result
            keyCertFile.upToDate = True

        self._keyCertFile = keyCertFile

        self.setResult("source", self)

    def queryFiles(self, query):
        url = 'http://localhost'
        project = 'CMIP5'
        results = esgf_utils.fetchData(
            esgf_utils.makeESGFSearchURL(url, project, query) ,query);
        return results

    def download(self, files):
        datalist = []
        for f in files:
            tmpfile = esgf_utils.extractFileNameFromURL(f["url"])
            if(esgf_utils.httpDownloadFile(self._keyCertFile.name, f["url"], tmpfile)):
                cdms = CDMSVariable()
                cdms.data_file = File();
                cdms.data_file.name = tmpfile;
                cdms.var_name = f["var"][0]["short_name"]
                cdms.var = vcs_util.get_variable(tmpfile, cdms.var_name)
                datalist[len(datalist):] = [cdms]
            else:
                print "Error downloading file %s" % f["url"]
        return datalist 

    _output_ports = [("source", "(%s:cpSource)" % identifier)]



class NetCDFToCSV(Module):
    _input_ports = [("variable", "(%s:CDMSVariable)" % identifier)]

    _output_ports = [("csv", "(edu.utah.sci.vistrails.basic:File)")]

    def compute(self):
        from csvDownload import convertNetCDFToCSV
        variable = self.getInputFromPort("variable")
        output = File()
        output.name = convertNetCDFToCSV(variable.data_file.name, variable.var_name)
        self.setResult("csv", output)

# ----------------------------------------------------------------------Modules
_modules = [WebSink, 
            (WebConfigSink, {'configureWidgetType': 
                             ('userpackages.climatepipes.widgets', 
                              'WebConfigSinkWidget')}),
            CDMSVariable, 
            CropImage, 
            (cpQuery, {'abstract': True}),
            Query,
            DataFile,
            GetFirstQueryData,
            QueryToJSON,
            NetCDFToCSV,
            (cpSource, {'abstract': True}),
            ESGFSource,
            KitwareSource,
            ESGFSearch,
            ESGFDownloadFile,
            (vcsPlot, {'abstract': True})]

# FIXME we should probably use uvcdat's code for this...
for plot_type in ['Boxfill', 'Isofill', 'Isoline', 'Meshfill', 'Outfill', \
                  'Outline', 'Scatter', 'Taylordiagram', 'Vector', 'XvsY', \
                  'Xyvsy', 'Yxvsx']:
    klass = type("vcs" + plot_type, (vcsPlot,),
                 {'plot_type': plot_type})
    _modules.append(klass)

def initialize():
    global web_out_dir, web_server_path

    if configuration.check('web_out_dir'):
        web_out_dir = configuration.web_out_dir
    if configuration.check('web_server_path'):
        web_server_path = configuration.web_server_path
