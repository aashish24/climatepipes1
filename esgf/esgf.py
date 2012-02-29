import myproxy_logon
import os
# import urllib2
import libxml2
import string
import subprocess
import time
import synonyms
import variable_score
import httplib2

# -----------------------------------------------------------------------------
def login():
    '''
    Predefined login parameters are used to generate a key/certificate if not
    already exists

    RETURN: The path to the key/certificate file. This can be treated as a handle.
    TODO: If the file exists check time it has been around for and if expired
          delete and regenerate.
    '''
    host = 'pcmdi3.llnl.gov'
    port = 2119
    user = 'nix'
    password = '2pw4kw'
    keyCertFile = '/tmp/keyCert.esgf'
    if(not(os.path.exists(keyCertFile))):
        print keyCertFile + " does not exist"
        try:
            myproxy_logon.myproxy_logon(host,
                                        user,
                                        password,
                                        keyCertFile,
                                        port=port)
        except Exception, err:
            print "Could not connect : ";
            return 0;
    return keyCertFile

# -----------------------------------------------------------------------------
def httpDownloadFile(keyCertFile,url,fnm):
    '''
    Download the given file from url and save it into fnm. The keyCertFile is
    used for authentication and typically got after some form of login process.
    '''
    cmd = "wget --certificate %s -t 2 -T 10 --private-key %s -O %s %s --no-check-certificate" % (keyCertFile,keyCertFile,fnm,url)
    pipe = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    time.sleep(.1)
    out,err = pipe.communicate()
    if(len(out)):
        return out
    else:
        return err
    
# -----------------------------------------------------------------------------
def prependQuery(str):
    '''
    Given an example string 'text' return  &query="text"
    '''
    return '&query="'+str+'"'
    
# -----------------------------------------------------------------------------
def makeESGFSearchURL(searchString):
    '''
    Takes a base url and searchString and returns a url to be used with ESGF
    '''
    q = "".join(map(prependQuery, synonyms.get_synonyms_strict(searchString)))
    return 'http://pcmdi9.llnl.gov/esg-search/search?project=CMIP5&index_node=pcmdi9.llnl.gov'+q

# -----------------------------------------------------------------------------
def fetchXML(url):
    '''
    Fetches data from the url. Cleanes all the "\n" characters and returns the
    clean string.
    '''
    # u = urllib2.urlopen(url)
    # data = u.read()
    
    resp, data = httplib2.Http().request(url)
 
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
def variableRank(diction, query):
    '''
    '''
    return {'name': diction['name'],
            "rank": variable_score.get_rank(diction['name'],query)}

# -----------------------------------------------------------------------------
def variablesRankAndSort(lst,query):
    '''
    '''
    return sorted(map((lambda x: variableRank(x,query)),lst),
                  key=lambda x:x['rank'],
                  reverse=True)

# -----------------------------------------------------------------------------
def fileRank(diction,query):
    '''
    '''
    variables = variablesRankAndSort(diction['variables'], query);
    return {'url': diction['url'],
            'var': variables,
            'rank' : variables[0]['rank']}

# -----------------------------------------------------------------------------
def filesRankAndSort(lst, query):
    '''
    '''
    return sorted(map((lambda x:fileRank(x,query)),lst),
                  key=lambda x:x['rank'],
                  reverse=True)
    
# -----------------------------------------------------------------------------
def fetchData(url,query):
    '''
    Fetches all relevand info from the given url
    '''
    return filesRankAndSort(merge(map(getCatalogData, getCatalog(fetchXML(url)))),
                            query)

# url = 'http://pcmdi9.llnl.gov/esg-search/search?project=CMIP5&index_node=pcmdi9.llnl.gov'
# data = fetchData(url)

# -----------------------------------------------------------------------------
# Extra code to test stuff

# import xml.etree.ElementTree as xml
# xdata = xml.fromstring(data)
# xml.dump(xdata)
