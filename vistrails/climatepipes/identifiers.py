from core.configuration import ConfigurationObject

identifier = 'org.vistrails.climatepipes'
version = '0.0.1'
name = 'ClimatePipes'

configuration = ConfigurationObject(web_server_path=(None,str),
                                    web_out_dir=(None, str))

def package_dependencies():
    return ['edu.utah.sci.vistrails.vtk']
