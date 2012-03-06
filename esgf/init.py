import os
import sys
sys.path.append(os.path.dirname(__file__))
import core.modules.module_registry
from core.modules.vistrails_module import Module, ModuleError
from core.modules.basic_modules import String, Integer, List, File
import esgf_utils


# ------------------------------------------------------------------------Login
class ESGFLogin(Module):
    '''
    ESGFLogin is used to login to ESGF
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
        
        self.setResult("keyCertFile", keyCertFile)

    _input_ports =[('host', "(edu.utah.sci.vistrails.basic:String)"),
                   ('port', "(edu.utah.sci.vistrails.basic:Integer)"),
                   ('user', "(edu.utah.sci.vistrails.basic:String)"),
                   ('password', "(edu.utah.sci.vistrails.basic:String)"),
                   ('keyCertFile', "(edu.utah.sci.vistrails.basic:File)")]
    _output_ports = [('keyCertFile', "(edu.utah.sci.vistrails.basic:File)")]

# -----------------------------------------------------------------------Search
class ESGFSearch(Module):
    '''
    ESGFSearch is a module that downloads metadata form ESGF.
    ''' 
    def compute(self):
        query = self.forceGetInputFromPort("query", None)
        url = self.force.GetInputFromPort("url",'http://pcmdi9.llnl.gov')
        project = self.force.GetInputFromPort("project",'CMIP5')
        result = esgf_utils.fetchData(esgf_utils.makeESGFSearchURL(url, project, query)
                                      ,query);
        self.setResult("value", result)
    
    _input_ports = [('query', "(edu.utah.sci.vistrails.basic:String)", True),
                    ('url', "(edu.utah.sci.vistrails.basic:String)")
                    ('project' "(edu.utah.sci.vistrails.basic:String)")]
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

        outputFile = esdf_utils.extractFileNameFromURL(url)
        # outputFile = self.interpreter.filePool.create_file(suffix='.nc')
        result = esgf_utils.httpDownloadFile(keyCertFile.name, url, outputFile.name)
        self.setResult("outputFile", outputFile)

    _input_ports = [('keyCertFile', "(edu.utah.sci.vistrails.basic:File)"),
                    ('url', "(edu.utah.sci.vistrails.basic:String)")]
    _output_ports = [('outputFile', "(edu.utah.sci.vistrails.basic:File)")]

# ----------------------------------------------------------------------Modules
_modules =[ESGFLogin,ESGFSearch,ESGFDownloadFile]
