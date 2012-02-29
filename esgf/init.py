import core.modules.module_registry
from core.modules.vistrails_module import Module, ModuleError
from core.modules.basic_modules import String, Integer, List
import esgf


# ------------------------------------------------------------------------Login
class ESGFLogin(Module):
    '''
    ESGFLogin is used to login to ESGF
    '''
    def compute(self):
        host = self.getInputFromPort("host")
        port = self.getInputFromPort("port")
        user = self.getInputFromPort("user")
        password = self.getInputFromPort("password")
        keyCertFile = self.getInputFromPort("keyCertFile")
        result = esgf.login()            # inputs are hardcoded function
        self.setResult("keyCertFile", result)

    _input_ports =[('host', String),
                   ('port', Integer),
                   ('user', String),
                   ('password', String),
                   ('keyCertFile',String)]
    _output_ports = [('keyCertFile', String)]

# -----------------------------------------------------------------------Search
class ESGFSearch(Module):
    '''
    ESGFSearch is a module that downloads metadata form ESGF.
    ''' 
    def compute(self):
        query = self.getInputFromPort("query")
        url = self.getInputFromPort("url")
        result = esgf.fetchData(url);
        self.setResult("value", result)
    
    _input_ports = [('query', String,True),
                    ('url', String )]
    _output_ports = [('value', List)]

# ---------------------------------------------------------------------Download
class ESGFDownloadFile(Module):
    '''
    Downloads specified files from ESGF. Needs ESGF key and fileName.
    '''
    def compute(self):
        keyCertFile = self.getInputFromPort("keyCertFile")
        url = self.getInputFromPort("url")
        fileName = self.getInputFromPort("fileName")
        result = esgf.httpDownloadFile(keyCertFile,url,fileName)
        self.setResult("value", result)

    _input_ports = [('keyCertFile',String),
                    ('url',String),
                    ('fileName',String)]
    _output_ports = [('value',String)]

# ----------------------------------------------------------------------Modules
_modules =[ESGFLogin,ESGFSearch,ESGFDownloadFile]
