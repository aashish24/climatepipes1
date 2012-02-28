import os
import shutil
import uuid

from core.modules.vistrails_module import Module, ModuleError
from core.modules.basic_modules import Constant, File

from identifiers import *

web_server_path = os.path.join( \
    os.environ.get("CATALINA_HOME", 
                   "/vistrails/climatepipes/paraviewweb/apache-tomcat-6.0.35"),
    "webapps")
web_out_dir = 'Climate/tmp'

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

_modules = [WebSink]
_subworkflows = ["vtkIsosurfaceOffscreen.xml"]

def initialize():
    global web_out_dir
                                        
    if configuration.check('web_out_dir'):
        web_out_dir = configuration.web_out_dir
    if configuration.check('web_server_path'):
        web_server_path = configuration.web_server_path
