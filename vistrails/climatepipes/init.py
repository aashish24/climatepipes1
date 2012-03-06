import os
import shutil
import uuid

from core.modules.vistrails_module import Module, ModuleError
from core.modules.basic_modules import Constant, File

from identifiers import *

from create_plot import *
from convert import *

web_server_path = os.path.join( \
    os.environ.get("CATALINA_HOME", 
                   "/vistrails/climatepipes/paraviewweb/apache-tomcat-6.0.35"),
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

class ClimateIsoFillParams(Module):
    _input_ports = [("file", "(edu.utah.sci.vistrails.basic:File)"),
                    ("var", "(edu.utah.sci.vistrails.basic:String)"),
                    ("lat", "(edu.utah.sci.vistrails.basic:Float,edu.utah.sci.vistrails.basic:Float)"),
                    ("lon", "(edu.utah.sci.vistrails.basic:Float,edu.utah.sci.vistrails.basic:Float)")]

    _output_ports = [("data", "(edu.utah.sci.vistrails.basic:List)")]

    def compute(self):
        if self.hasInputFromPort("file"):
            f = self.getInputFromPort("file")
            var = self.forceGetInputFromPort("var", None)
            lat = self.forceGetInputFromPort("lat", None)
            lon = self.forceGetInputFromPort("lon", None)

            self.setResult("data", [[f, var, lat, lon]])

##############################################################################

class ClimateIsoFill(Module):
    _input_ports = [("data", "(edu.utah.sci.vistrails.basic:List)")]

    _output_ports = [("image", "(edu.utah.sci.vistrails.basic:File)")]

    def compute(self):
        if self.hasInputFromPort("data"):
            data = self.getInputFromPort("data")
            #data is an Nx4 array, each row represents a data file and its info
            #we just use the top of the list for this visualization
            topdata = data[0]
            datafile = topdata[0]
            datavar = topdata[1]
            lat = topdata[2]
            lon = topdata[3]

            if isinstance(datafile, File):
                suffix = os.path.splitext(datafile.name)[1][1:]
                if suffix != "nc":
                    raise ModuleError(self, "Error: Invalid file type. Expecting '.nc' and got '.%s'" % suffix)
            
                output = self.interpreter.filePool.create_file(suffix='.png')   
                vcsiso = create_vcs_isofill(datafile.name, datavar, lat, lon, output.name)
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

_modules = [WebSink, ClimateIsoFill, ClimateIsoFillParams, CropImage]
_subworkflows = ["Visualize.xml"]

def initialize():
    global web_out_dir
                                        
    if configuration.check('web_out_dir'):
        web_out_dir = configuration.web_out_dir
    if configuration.check('web_server_path'):
        web_server_path = configuration.web_server_path
