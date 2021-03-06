
# Import python module
import base64
import os
import sys
import uuid

# Global variable
_currDir = ''
_dataDir = ''
_tmpDir = ''
_outputFilePath = ''

_vtHome = os.environ['VISTRAILS_HOME']
_pyQt4Home = os.environ['PYQT4_HOME']
_tmpDir = os.environ['CP_TMP_DIR']

sys.path.append(_vtHome)
sys.path.append(_pyQt4Home)
sys.argv = []

# Import vistrails module
import core.api
import core.application as vt_app
import core.db.action
# DAK -- I use a separate .vistrails directory for my command-line work...
# vt_app.init({'dotVistrails': '/Users/dakoop/.vistrails.cmdline'})
from core.vistrail.pipeline import Pipeline
from core.vistrail.vistrail import Vistrail
from core.db.locator import FileLocator
from core.packagemanager import get_package_manager
from core.api import get_api
from core.modules.vistrails_module import Module

class cpApp(object):
    def __init__(self):
        sys.argv = []
        #QtGui.QApplication.__init__(self, sys.argv)
    # -------------------------------------------------------------------------
    def init(self):
      global _currDir
      global _dataDir
      global _vtHome

      # This is not set as the script is embedded and hence in order to
      # avoid running into issues of undefined, setting it null for now
      sys.argv = []

      # Find vistrails root dir as we need it for core vt module
      _vtHome = os.environ['VISTRAILS_HOME']
      sys.path.append(_vtHome)

      _currDir = os.getcwd()
      _dataDir = os.environ['CP_DATA_DIR']      

      vt_app.init()

    # -------------------------------------------------------------------------
    def processWorkFlow(self, xmlFile):
      global _outputFilePath

      # there should probably be a call in the api for this block of code
      vistrail = Vistrail()
      locator = FileLocator(xmlFile)
      workflow = locator.load(Pipeline)

      action_list = []
      for module in workflow.module_list:
        if module.name == 'FileSink':
           _outputFilePath = _tmpDir + '/cp_tmp_' + uuid.uuid4().hex + '.png'
           for i in xrange(module.getNumFunctions()):
             if 'outputPath' == module.functions[i].name:
               module.functions[i].params[0].strValue = _outputFilePath;

        action_list.append(('add', module))

      for connection in workflow.connection_list:
        action_list.append(('add', connection))

      action = core.db.action.create_action(action_list)
      vistrail.add_action(action, 0L)
      vistrail.update_id_scope()
      vistrail.addTag("Imported workflow", action.id)

      vt = get_api()

      # there should probably be a call in the api for this next line
      vt._controller.set_vistrail(vistrail, locator)
      vt.select_version(action.id)

      # Assuming that this call is synchronou
      vt.execute()

      # Close and exit
      vt.close_vistrail()

    #@pyqtSlot()
    # -------------------------------------------------------------------------
    def process(self, filePath=None):
      if(filePath == None):
          return
      # Initialize alway
      self.init()

      return self.processWorkFlow(filePath)    

# Execute and process incoming message
# -----------------------------------------------------------------------------
def execute(message):
  # Assuming that message is a XML workflow
  xmlFilePath = _tmpDir + '/cp_tmp_' + uuid.uuid4().hex + '.xml'
  file = open(xmlFilePath, 'w')
  file.write(message);
  file.close();

  app = cpApp();
  app.process(xmlFilePath);

  # No longer need the workflow file
  os.remove(xmlFilePath)

  file = open(_outputFilePath, 'rb')
  try:
    imageData = file.read()
    imageData = base64.b64encode(imageData)
    return imageData
  finally:
    file.close()    
    os.remove(_outputFilePath)

# Return binary image data
# -----------------------------------------------------------------------------
def testGetImageBinaryData():
  filePath = _dataDir + '/files/test.png'
  file = open(filePath, 'rb')
  imageData = file.read()
  imageData = base64.b64encode(imageData)
  return imageData
