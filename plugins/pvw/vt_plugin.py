import os
import StringIO
import sys
import uuid

_vtHome = os.environ.get("VISTRAILS_HOME", "/vistrails/src/git/vistrails")
_tmpDir = os.environ.get("VT_TMP_DIR", "/tmp")
_vtOptions = {'dotVistrails': '/Users/dakoop/.vistrails.cmdline'}

sys.path.append(_vtHome)
sys.path.append('/vistrailsinc/paraview_src/ParaView/build/Utilities/VTKPythonWrapping/site-packages/paraview')
import core.application as vt_app
vt_app.init(_vtOptions)
from core.api import get_api

def execute(wf_xml):
    session = uuid.uuid4().hex
    wf_xml_fname = os.path.join(_tmpDir, "vt_wf_%s.xml" % session)
    # out_fname = os.path.join(_tmpDir, "vt_out_%s.txt" % session)
    result = None
    try:
        # dump the wf_xml to a file
        f = open(wf_xml_fname, 'w')
        f.write(wf_xml)
        f.close()

        vt = get_api()
        vt.load_workflow(wf_xml_fname)
        
        # hijack stdout and dump it to a file
        sys.stdout = StringIO.StringIO()
        # sys.stdout = open(out_fname, 'w')
        vt.execute()
        result = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        
        vt.close_vistrail()
        # result = open(out_fname).read()
    # except Exception, e:
    #     f = open('/tmp/test.error', 'w')
    #     print >>f, e
    #     f.close()
    finally:
        # cleanup
        if os.path.exists(wf_xml_fname):
            os.unlink(wf_xml_fname)
        # if os.path.exists(out_fname):
        #     os.unlink(out_fname)
    # f = open('/tmp/test.out', 'w')
    # print >>f, result
    # f.close()
    return result
