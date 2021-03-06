import cdms2
import vcs
import os

#fnm = '/home/aashish/tools/cdat/install/sample_data/clt.nc'
def create_vcs_isofill(filename, varname, lat, lon,  out_fname):
    f = cdms2.open(filename)
    # print f.listvariables()

    if varname is None:
        # Guess varname by searching through avaiable vars and seeing if the 
        # filename contains it. Defaults to "clt".
        base = os.path.basename(filename)
        for var in f.listvariables():
            if base.find(var) > -1:
                varname = var
        if varname is None:
            varname = "clt"
            
    s=f(varname)

    # Define the axis
    if lat is None:
        lat = (-90.0, 90.0)
    if lon is None:
        lon = (-180.0, 175.0)
    s=s(latitude=lat,squeeze=1,longitude=lon,)

    # Create the plot
    x=vcs.init()
    iso=x.createisofill()

    # Turn off everything, we are interested only in the data
    t=x.createtemplate()
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
    p=x.createprojection()
    p.type="linear"
    # prints possible attribute for mercator, you'll need to know what you're doing here.
    #p.list()
    iso.projection=p

    # Set plot dimensions
    x.setbgoutputdimensions(width=2000,units="pixel")
    x.plot(s,iso,t,bg=1,continents=1,ratio="auto")
    # x.plot(s,iso,t,continents=1,ratio="auto")

    x.png(out_fname)
    # return x

if __name__ == '__main__':
    import sys
    if sys.platform == 'darwin':
        from PyQt4 import QtGui
        app = QtGui.QApplication([])
    create_vcs_isofill('/vistrails/uvcdat/src/cdat/install/sample_data/clt.nc',
                       '/tmp/foo.png')

    if sys.platform == 'darwin':
        app.quit()
