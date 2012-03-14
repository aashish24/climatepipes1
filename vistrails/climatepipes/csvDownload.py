from Scientific.IO.NetCDF import NetCDFFile
import os

# -----------------------------------------------------------------------------
def getCSVFileName(netCDFFile, varname):
    '''
    Replace file name with .nc extension with .csv
    '''
    return netCDFFile.split('.nc')[0]+ "_" + varname + ".csv"

# -----------------------------------------------------------------------------
def getNetCDFFileName(csvFile):
    '''
    '''
    return csvFile.split('csv')[0]+".nc"

# -----------------------------------------------------------------------------
def convertNetCDFToCSV(netCDFFileName,variable):
    '''
    '''
    csvFileName = getCSVFileName(netCDFFileName, variable)

    # Check if the file has already been converted
    if(os.path.isfile(csvFileName)):
        return csvFileName

    f = NetCDFFile(netCDFFileName)             # read file
    lat = f.variables['lat'].getValue()        # extract lattitute
    lon = f.variables['lon'].getValue()        # extract longitude
    data = f.variables[variable].getValue()[0] # extract variable data for
    out = open(csvFileName, 'w')
    print >> out, '''"lat","lon","data"'''
    for i in range(len(lat)):
        for j in range(len(lon)):
            # print lat[i] ,',', lon[j] ,',', data[i][j]
            print >> out , lat[i] ,',', lon[j] ,',', data[i][j]
    out.close()
    return csvFileName
