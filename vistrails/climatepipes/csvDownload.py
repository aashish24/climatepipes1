from Scientific.IO.NetCDF import NetCDFFile

# -----------------------------------------------------------------------------
def getCSVFileName(netCDFFile):
    '''
    Replace file name with .nc extension with .csv
    '''
    return netCDFFile.split('.nc')[0]+".csv"

# -----------------------------------------------------------------------------
def getNetCDFFileName(csvFile):
    '''
    '''
    return csvFile.split('csv')[0]+".nc"

# -----------------------------------------------------------------------------
def convertNetCDFToCSV(netCDFFileName,variable):
    '''
    '''
    f = NetCDFFile(netCDFFileName)             # read file
    lat = f.variables['lat'].getValue()        # extract lattitute
    lon = f.variables['lon'].getValue()        # extract longitude
    data = f.variables[variable].getValue()[0] # extract variable data for
    # print getCSVFileName(netCDFFileName)
    out = open(getCSVFileName(netCDFFileName), 'w')
    print >> out, '''"lat","lon","data"'''
    for i in range(len(lat)):
        for j in range(len(lon)):
            # print lat[i] ,',', lon[j] ,',', data[i][j]
            print >> out , lat[i] ,',', lon[j] ,',', data[i][j]
    out.close()
