import myproxy_logon
import httplib
import os
import urllib2
import urlparse
import libxml2
import string
import subprocess
import time

from ndg.httpsclient.utils import open_url, Configuration
from ndg.httpsclient import ssl_context_util


stashedKeyCertFname = None

# -----------------------------------------------------------------------------
def login(host=None, port=None, user=None, password=None, keyCertFile=None):
    '''
    Predefined login parameters are used to generate a key/certificate if not
    already exists

    RETURN: The path to the key/certificate file. This can be treated as a handle.
    TODO: If the file exists check time it has been around for and if expired
          delete and regenerate.
    '''
    if host is None:
        host = 'pcmdi3.llnl.gov'
    if port is None:
        port = 2119
    if user is None:
        user = 'nix'
    if password is None:
        password = '2pw4kw'
    if keyCertFile is not None and os.path.getsize(keyCertFile) > 0:
        return keyCertFile
    elif stashedKeyCertFname is not None:
        return stashedKeyCertFname
    elif keyCertFile is None:
        keyCertFile = '/tmp/keyCert.esgf'

    # let the exception propogate, it will be caught and shown as error
    myproxy_logon.myproxy_logon(host,
                                user,
                                password,
                                keyCertFile,
                                port=port)
    return keyCertFile

# -----------------------------------------------------------------------------
def httpDownloadFile(keyCertFile, url, fnm): #url,fnm):
    '''
    Download the given file from url and save it into fnm. The keyCertFile is
    used for authentication and typically got after some form of login process.
    '''
    ssl_context = ssl_context_util.make_ssl_context(keyCertFile, 
                                                    keyCertFile,
                                                    None,
                                                    None,
                                                    False,
                                                    url)
    config = Configuration(ssl_context, False)
    return_code, return_msg, response = open_url(url, config)
    if return_code == httplib.OK:
        try:
            file_size = int(response.info().getheaders("Content-Length")[0])
        except:
            file_size = -1

        print "Downloading %d Bytes" % file_size
        file_size_dl = 0
        f = open(fnm, 'w')
        while True:
            buf = response.read(8192)
            if not buf:
                break
            f.write(buf)
            file_size_dl += len(buf)
            status = "%10d [%3.2f%%]" % (file_size_dl, 
                                         file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status,
        f.close()
        response.close()
        return True
    return False

# -----------------------------------------------------------------------------
def fetchXML(url):
    '''
    Fetches data from the url. Cleanes all the "\n" characters and returns the
    clean string.
    '''
    u = urllib2.urlopen(url)
    data = u.read()
    data=string.replace(data, "\r\n", "")
    data=string.replace(data, "\n", "")
    return data

# -----------------------------------------------------------------------------
def getCatalog(stringDoc):
    '''
    Gets all the catelogs from a string document
    '''
    doc = libxml2.parseDoc(stringDoc)
    return [attr.content for attr in doc.xpathEval("/response/result//arr[@name='url']/str[1]")]

# -----------------------------------------------------------------------------
def getURLAndVariables(context,attr):
    '''
    Internal funciton to get the url and the variables available in a datafile
    '''
    context.setContextNode(attr)
    url = context.xpathEval("./@urlPath")[0]
    return {"url":'http://pcmdi9.llnl.gov/thredds/fileServer/'+url.content,
            "variables":[{"name":i.content,"rank":0} for i in context.xpathEval("./ns:variables/ns:variable[@name]")],
            "rank":0}

# -----------------------------------------------------------------------------
def getMetadataAndFiles(stringDoc):
    '''
    Gets the metadata [variables] and files available in esgf catalog
    '''
    context = libxml2.parseDoc(stringDoc).xpathNewContext()
    context.xpathRegisterNs("ns","http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0")
    # variables = [{"variable":attr.content, "rank":0} for attr in context.xpathEval("/ns:catalog/ns:dataset/ns:variables/ns:variable[@name]")]
    # print variables
    files=[]
    for attr in context.xpathEval("/ns:catalog/ns:dataset/ns:dataset[@urlPath]"):
        files[len(files):] =  [getURLAndVariables(context,attr)]
    return files

# -----------------------------------------------------------------------------
def getCatalogData(url):
    '''
    Fetches the catalog data from url and returns a list of dictionaries 
    '''
    return getMetadataAndFiles(fetchXML(url))

 # -----------------------------------------------------------------------------
def merge(seq):
    '''
    Merge a sequence of lists into a single one.
    '''
    merged = []
    for s in seq:
        for x in s:
            merged.append(x)
    return merged

# -----------------------------------------------------------------------------
def fetchData(url):
    '''
    Fetches all relevand info from the given url
    '''
    return merge(map(getCatalogData, getCatalog(fetchXML(url))))

# url = 'http://pcmdi9.llnl.gov/esg-search/search?project=CMIP5&index_node=pcmdi9.llnl.gov'
# data = fetchData(url)

# -----------------------------------------------------------------------------
# Extra code to test stuff

# import xml.etree.ElementTree as xml
# xdata = xml.fromstring(data)
# xml.dump(xdata)
