import os
import shutil
import uuid

from core.modules.vistrails_module import Module, ModuleError
from core.modules.basic_modules import Constant, File

from identifiers import *

import vcs_util
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

# class ClimateIsoFill(Module):
#     _input_ports = [("data", "(edu.utah.sci.vistrails.basic:File)"),
#                     ("variable", "(edu.utah.sci.vistrails.basic:String)"),
#                     ("data_list", "(edu.utah.sci.vistrails.basic:List)")]

#     _output_ports = [("image", "(edu.utah.sci.vistrails.basic:File)")]

#     def compute(self):
#         if self.hasInputFromPort("data"):
#             data = self.getInputFromPort("data")
#         elif self.hasInputFromPort("data_list"):
#             data = self.getInputFromPort("data_list")[0]
#         else:
#             raise ModuleError(self, 
#                               'Missing value from both port data and data_list')
#         var = self.getInputFromPort("variable")

#         if isinstance(data, File):
#             suffix = os.path.splitext(data.name)[1][1:]
#             if suffix != "nc":
#                 raise ModuleError(self, "Error: Invalid file type. Expecting '.nc' and got '.%s'" % suffix)
            
#             output = self.interpreter.filePool.create_file(suffix='.png')   
#             vcsiso = create_vcs_isofill(data.name, variable, output.name)
#             self.setResult("image", output)


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

_modules = [WebSink, CDMSVariable, (vcsPlot, {'abstract': True}), CropImage, First]
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
