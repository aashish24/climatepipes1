
# Import python modules
import sys
import os
import base64

# Global variables
_currDir = ''
_dataDir = ''
_tmpDir = ''
_message = ''
_vtHome = os.environ['VISTRAILS_HOME']
sys.path.append(_vtHome)

# Import vistrails modules
import core.api
import core.application as vt_app
import core.db.action
# DAK -- I use a separate .vistrails directory for my command-line work...# vt_app.init({'dotVistrails': '/Users/dakoop/.vistrails.cmdline'})
from core.vistrail.pipeline import Pipeline
from core.vistrail.vistrail import Vistrail
from core.db.locator import FileLocator
from core.packagemanager import get_package_manager
from core.api import get_api
from PyQt4 import QtGui, QtCore, QtNetwork
from PyQt4.QtCore import pyqtSlot

class cpApp(QtGui.QApplication):
    def __init__(self):
        QtGui.QApplication.__init__(self, sys.argv)

    def init(self):
      global _currDir
      global _dataDir
      global _tmpDir
      global _vtHome

      # This is not set as the script is embedded and hence in order to
      # avoid running into issues of undefined, setting it null for now
      sys.argv = []

      # Find vistrails root dir as we need it for core vt modules
      _vtHome = os.environ['VISTRAILS_HOME']
      sys.path.append(_vtHome)

      _currDir = os.getcwd()
      _dataDir = os.environ['CP_DATA_DIR']
      _tmpDir = os.environ['CP_TMP_DIR']

      # Check if the package has been enabled or not
      # This needs to get done only once
      #pm = get_package_manager()
      #qpm.late_enable_package('text')
      import gui.theme
      gui.theme.initializeCurrentTheme()

      vt_app.init()

    def processWorkFlow(self, xmlFile):
      print 'input is', xmlFile

      # there should probably be a call in the api for this block of code
      vistrail = Vistrail()
      locator = FileLocator(xmlFile)
      workflow = locator.load(Pipeline)

      action_list = []
      for module in workflow.module_list:
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

      # Assuming that this call is synchronous
      vt.execute()

      # Close and exit
      vt.close_vistrail()
      QtGui.QApplication.quit()

    @pyqtSlot()
    def process(self, message=None):

      if(message == None):
          message = _message

      # Initialize always
      self.init()

      return self.processWorkFlow(message)

      out_data = {}
      vt = core.api.get_api()
      text = vt.get_package("org.vistrails.text")
      basic = vt.get_package("edu.utah.sci.vistrails.basic")
      m1 = text.MergeFiles()
      m1.addFile(_dataDir + "/files/a.txt")
      m1.addFile(_dataDir + "/files/b.txt")

      m2 = basic.FileSink()
      m2.overwrite = True

      # For now dump output in the working directory
      outputPath = _tmpDir + '/c.txt'

      m2.outputPath = outputPath
      m2.file = m1.outputFile
      vt.tag_version("Merge1")
      vt.execute()

      vt.save_vistrail(_tmpDir + "/helloworld.vt")

      out_data['type'] = 'file'

      f = open(outputPath)

      try:
        out_data['data'] = f.read()
      finally:
        f.close()

      return out_data

# Execute and process incoming message
def execute(message):
  global _message
  _message = message
  app = cpApp();
  QtCore.QTimer.singleShot(2000, app, QtCore.SLOT("process()"));
  return app.exec_()

# Return binary image data
def testGetImageBinaryData():
  filePath = _dataDir + '/files/test.png'
  file = open(filePath, 'rb')
  imageData = file.read()
  imageData = base64.b64encode(imageData)
  return imageData
