import os, sys
import shutil
import uuid

from core.modules.vistrails_module import Module, ModuleError
from core.modules.basic_modules import Constant, File, String, Integer, List
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


##############################################################################

class CDMSVariable(Module):
    _input_ports = [("data", "(edu.utah.sci.vistrails.basic:File)"),
                    ("variable", "(edu.utah.sci.vistrails.basic:String)")]
    _output_ports = [("value", "(%s:CDMSVariable)" % identifier)]

    def compute(self):
        data = self.getInputFromPort("data")
        var_name = self.getInputFromPort("variable")
        self.var = vcs_util.get_variable(data.name, var_name)
        self.setResult("value", self)

class First(Module):
    '''
    Outputs the first cdms var from the list, or just passes the var
    '''
    _input_ports = [("list", "(edu.utah.sci.vistrails.basic:List)"),
                    ("var", "(%s:CDMSVariable)" % identifier)]

    _output_ports = [("value", "(%s:CDMSVariable)" % identifier)]

    def compute(self):
        if self.hasInputFromPort("var"):
            self.setResult("value", self.getInputFromPort("var"))
        else:
            _list = self.getInputFromPort("list")
            first = _list[0]
            self.setResult("value", first)

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
                    print "Error: Invalid file type. Expecting '.png' and got '.%s'" % suffix
                    return

                img = crop_whitespace(image.name)
                output = self.interpreter.filePool.create_file(suffix='.png')
                img.save(output.name, "PNG")

                self.setResult("image", output)

##############################################################################

#-------------------------------------------------------------------------Source
class cpSource(Module):
    '''
    Base class for source modules. 
    Subclasses should implement query and download.
    '''

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
        if self.hasInputFromPort("keyCertFile"):
            keyCertFile = self.getInputFromPort("keyCertFile")
            if not os.path.exists(keyCertFile.name):
                raise ModuleError(self,
                                  'Key certificate "%s" does not exist' % \
                                      keyCertFile.name)
        else:
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
                cdms.var = vcs_util.get_variable(tmpfile, f["var"][0]["short_name"])
                datalist[len(datalist):] = [cdms]
            else:
                print "Error downloading file %s" % f["url"]
        return datalist        

    _input_ports =[('host', "(edu.utah.sci.vistrails.basic:String)"),
                   ('port', "(edu.utah.sci.vistrails.basic:Integer)"),
                   ('user', "(edu.utah.sci.vistrails.basic:String)"),
                   ('password', "(edu.utah.sci.vistrails.basic:String)"),
                   ('keyCertFile', "(edu.utah.sci.vistrails.basic:File)")]

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
class Query(Module):
    '''
    Finds files on a source and either downloads or lists them based on
    connected input and output ports
    '''
    def compute(self):
        source = self.getInputFromPort("source")
        keywords = self.getInputFromPort("keywords")
#        datefrom = self.getInputFromPort("datefrom")
#        dateto = self.getInputFromPort("dateto")
#        location = self.getInputFromPort("location")
        numitems = self.forceGetInputFromPort("numitems", 1)

        #TODO: combine parameters to create query
        query = keywords
        
        results = source.queryFiles(query)
        results = results[0:numitems] #truncate results

        self.setResult('files', results)

        #if self.outputPorts('datalist'):
        datalist = source.download(results)
        self.setResult('data', datalist)


    _input_ports = [('source', "(%s:cpSource)" % identifier),
                    ('keywords', "(edu.utah.sci.vistrails.basic:String)"),
                    # ('datefrom', "(edu.utah.sci.vistrails.basic:String)"),
                    # ('dateto', "(edu.utah.sci.vistrails.basic:String)"),
                    # ('location', "(edu.utah.sci.vistrails.basic:String)"),
                    ('numitems', "(edu.utah.sci.vistrails.basic:Integer)")]
                   

    _output_ports = [('data', "(edu.utah.sci.vistrails.basic:List)"),
                     ('files', "(edu.utah.sci.vistrails.basic:List)")]

# ----------------------------------------------------------------------Modules
_modules = [WebSink, 
            CDMSVariable, 
            (vcsPlot, {'abstract': True}), 
            CropImage, 
            First,
            (cpSource, {'abstract': True}),
            ESGFSource,
            ESGFSearch,
            ESGFDownloadFile,
            Query]

# FIXME we should probably use uvcdat's code for this...
for plot_type in ['Boxfill', 'Isofill', 'Isoline', 'Meshfill', 'Outfill', \
                  'Outline', 'Scatter', 'Taylordiagram', 'Vector', 'XvsY', \
                  'Xyvsy', 'Yxvsx']:
    klass = type("vcs" + plot_type, (vcsPlot,),
                 {'plot_type': plot_type})
    _modules.append(klass)

def initialize():
    global web_out_dir

    if configuration.check('web_out_dir'):
        web_out_dir = configuration.web_out_dir
    if configuration.check('web_server_path'):
        web_server_path = configuration.web_server_path
