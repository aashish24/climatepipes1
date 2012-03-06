
def execute(wf_xml):
    import os
    import StringIO
    import sys
    import uuid

    _vtHome = os.environ.get("VISTRAILS_HOME", "/vistrails/src/git/vistrails")
    _tmpDir = os.environ.get("VT_TMP_DIR", "/tmp")
#    _vtOptions = {'dotVistrails': '/Users/dakoop/.vistrails.cmdline'}
    _vtOptions = {'dotVistrails': '/home/benbu/.vistrails'}

    sys.path.append(_vtHome)
    sys.path.append('/vistrailsinc/paraview_src/ParaView/build/Utilities/VTKPythonWrapping/site-packages/paraview')
    print >>sys.__stdout__, "RUNNING INIT"
    import core.application as vt_app
    vt_app.init(_vtOptions)
    print >>sys.__stdout__, "DONE WITH INIT"
    from core.api import get_api

    class DupOutput(StringIO.StringIO):
        def write(self, *args, **kwargs):
            sys.__stdout__.write(*args, **kwargs)
            StringIO.StringIO.write(self, *args, **kwargs)

        def writelines(self, *args, **kwargs):
            sys.__stdout__.writelines(*args, **kwargs)
            StringIO.StringIO.writelines(self, *args, **kwargs)

        def flush(self, *args, **kwargs):
            sys.__stdout__.flush(*args, **kwargs)
            StringIO.StringIO.flush(self, *args, **kwargs)


    print >>sys.__stdout__, "STARTING EXECUTE"
    print >>sys.__stdout__, "NEXT LINE"
    if sys.platform == 'darwin':
        from PyQt4 import QtGui
        app = QtGui.QApplication([])
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
        sys.stdout = DupOutput()
        # sys.stdout = open(out_fname, 'w')
        print >>sys.__stdout__, "Starting execution"
        vt.execute()
        sys.stdout.flush()
        print >>sys.__stdout__, "Done executing"
        result = sys.stdout.getvalue()
        print >>sys.__stdout__, "Result:", result
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        print >>sys.__stdout__, "Closing vistrail"
        vt.close_vistrail()
        print >>sys.__stdout__, "Done closing vistrail"
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
        # if sys.platform == 'darwin':
        #     app.quit()
        vt_app.finalize_vistrails(None)
        print >>sys.__stdout__, "Returning result"
        return result
    vt_app.finalize_vistrails(None)
    print >>sys.__stdout__, "Returning result"
    return result
