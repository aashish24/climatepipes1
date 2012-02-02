from paraview import simple as pv

_url = '' 

def setDataURL(url):
  global _url
  _url = url
  print 'URL is : ', _url

def getDataURL():
  return _url

def hello(name):
   return ['Hello ' + name, "54", 5, 'hioyhui']
