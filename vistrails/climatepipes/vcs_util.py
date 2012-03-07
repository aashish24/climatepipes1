import cdms2
import vcs

def get_variable(cdms_fname, var_name):
    f = cdms2.open(cdms_fname)
    v = f(var_name)
    return v

def get_variable_list(cdms_fname):
    f = cdms2.open(cdms_fname)
    return f.variables.keys()

def plot(plot_type, out_fname, var1, var2=None):
    # Define the axis
    var1 = var1(latitude=(-90.0, 90.0),squeeze=1,longitude=(-180.0, 175.0),)
    if var2 is not None:
        var2 = var2(latitude=(-90.0, 90.0),squeeze=1,longitude=(-180.0, 175.0),)

    # Create the plot
    v = vcs.init()
    create_method = getattr(v, 'create%s' % plot_type.lower())
    p = create_method()

    # Turn off everything, we are interested only in the data
    t = v.createtemplate()
    t.file.priority=0
    t.source.priority=0
    t.dataname.priority=0
    t.title.priority=0
    t.units.priority=0
    t.crdate.priority=0
    t.crtime.priority=0
    t.comment1.priority=0
    t.comment2.priority=0
    t.comment3.priority=0
    t.comment4.priority=0
    t.xname.priority=0
    t.yname.priority=0
    t.zname.priority=0
    t.tname.priority=0
    t.xunits.priority=0
    t.yunits.priority=0
    t.zunits.priority=0
    t.tunits.priority=0
    t.xvalue.priority=0
    t.yvalue.priority=0
    t.zvalue.priority=0
    t.tvalue.priority=0
    t.mean.priority=0
    t.min.priority=0
    t.max.priority=0
    t.xtic1.priority=0
    t.xtic2.priority=0
    t.xmintic1.priority=0
    t.xmintic2.priority=0
    t.ytic1.priority=0
    t.ytic2.priority=0
    t.ymintic1.priority=0
    t.ymintic2.priority=0
    t.xlabel1.priority=0
    t.xlabel2.priority=0
    t.ylabel1.priority=0
    t.ylabel2.priority=0
    t.line1.priority=0
    t.line2.priority=0
    t.line3.priority=0
    t.line4.priority=0
    t.box1.priority=0
    t.box2.priority=0
    t.box3.priority=0
    t.box4.priority=0
    t.logicalmask=0
    t.legend.priority=0
    t.data.x1=0.001
    t.data.x2=0.999
    t.data.y1=0.001
    t.data.y2=0.999

    # We need euclidean projection
    proj = v.createprojection()
    proj.type="linear"

    # prints possible attribute for mercator, you'll need to know what
    # you're doing here.
    # proj.list()
    p.projection = proj

    # Set plot dimensions
    v.setbgoutputdimensions(width=2000,units="pixel")
    if var2 is None:
        v.plot(var1, p, t, bg=1, continents=1, ratio="auto")
    else:
        v.plot(var1, var2, p, t, bg=1, continents=1, ratio="auto")

    v.png(out_fname)

if __name__ == '__main__':
    import sys
    if sys.platform == 'darwin':
        from PyQt4 import QtGui
        app = QtGui.QApplication([])
    #clt_fname = '/vistrails/uvcdat/src/cdat/install/sample_data/clt.nc'
    clt_fname = '/cp/cdat/install/sample_data/clt.nc'
    print get_variable_list(clt_fname)
    clt = get_variable(clt_fname, 'clt')
    u = get_variable(clt_fname, 'u')
    v = get_variable(clt_fname, 'v')

    plot('isofill', '/tmp/foo.png', clt)
    plot('xvsy', '/tmp/foo2.png', u, v)

    if sys.platform == 'darwin':
        app.quit()
