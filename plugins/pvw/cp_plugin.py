import sys
import os

_currDir = ''
_dataDir = ''
_tmpDir = ''
_vtHome = ''

def init():
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

def process(message):
  init()

  import core.api
  import core.application as vt_app
  from core.packagemanager import get_package_manager

  out_data = {}
  vt_app.init()
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

def execute(message):
  return process(message)
