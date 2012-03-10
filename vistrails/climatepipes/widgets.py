from gui.modules.source_configure import SourceConfigurationWidget
from gui.modules.python_source_configure import PythonEditor


class WebConfigSinkWidget(SourceConfigurationWidget):
    def __init__(self, module, controller, parent=None):
        """ WebConfigSinkWidget(module: Module,
                                controller: VistrailController,
                                parent: QWidget)
                                -> WebConfigSinkWidget
        Setup the dialog to similar to PythonSource but with a
        different name
        
        """
        SourceConfigurationWidget.__init__(self, module, controller, 
                                           PythonEditor, True, False, parent)
