var esgf_modules = [
 {
  "category": "com-kitware-climatepipes-esgf", 
  "container": {
   "fields": [
    {
     "alias": "", 
     "vtype": "edu.utah.sci.vistrails.basic:File", 
     "type": "string", 
     "inputParams": {
      "required": true, 
      "name": "keyCertFile", 
      "label": "keyCertFile"
     }
    }, 
    {
     "alias": "", 
     "vtype": "edu.utah.sci.vistrails.basic:String", 
     "type": "string", 
     "inputParams": {
      "required": true, 
      "name": "url", 
      "label": "url"
     }
    }
   ], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "keyCertFile", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(edu.utah.sci.vistrails.basic:File)", 
      "allowedTypes": [
       "o(edu.utah.sci.vistrails.basic:File)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "url", 
     "offsetPosition": {
      "top": -15, 
      "left": 213.33333333333334
     }, 
     "ddConfig": {
      "type": "i(edu.utah.sci.vistrails.basic:String)", 
      "allowedTypes": [
       "o(edu.utah.sci.vistrails.basic:String)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "outputFile", 
     "offsetPosition": {
      "bottom": -15, 
      "left": 160.0
     }, 
     "ddConfig": {
      "type": "o(edu.utah.sci.vistrails.basic:File)", 
      "allowedTypes": [
       "i(edu.utah.sci.vistrails.basic:File)", 
       "i(edu.utah.sci.vistrails.basic:Path)", 
       "i(edu.utah.sci.vistrails.basic:Constant)", 
       "i(edu.utah.sci.vistrails.basic:Module)"
      ]
     }
    }
   ], 
   "vt": {
    "cache": 1, 
    "namespace": "", 
    "version": "0.9.0", 
    "package": "com.kitware.climatepipes.esgf"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "ESGFDownloadFile"
 }, 
 {
  "category": "com-kitware-climatepipes-esgf", 
  "container": {
   "fields": [
    {
     "alias": "", 
     "vtype": "edu.utah.sci.vistrails.basic:String", 
     "type": "string", 
     "inputParams": {
      "required": true, 
      "name": "host", 
      "label": "host"
     }
    }, 
    {
     "alias": "", 
     "vtype": "edu.utah.sci.vistrails.basic:Integer", 
     "type": "string", 
     "inputParams": {
      "required": true, 
      "name": "port", 
      "label": "port"
     }
    }, 
    {
     "alias": "", 
     "vtype": "edu.utah.sci.vistrails.basic:String", 
     "type": "string", 
     "inputParams": {
      "required": true, 
      "name": "user", 
      "label": "user"
     }
    }, 
    {
     "alias": "", 
     "vtype": "edu.utah.sci.vistrails.basic:String", 
     "type": "string", 
     "inputParams": {
      "required": true, 
      "name": "password", 
      "label": "password"
     }
    }, 
    {
     "alias": "", 
     "vtype": "edu.utah.sci.vistrails.basic:File", 
     "type": "string", 
     "inputParams": {
      "required": true, 
      "name": "keyCertFile", 
      "label": "keyCertFile"
     }
    }
   ], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "host", 
     "offsetPosition": {
      "top": -15, 
      "left": 53.333333333333336
     }, 
     "ddConfig": {
      "type": "i(edu.utah.sci.vistrails.basic:String)", 
      "allowedTypes": [
       "o(edu.utah.sci.vistrails.basic:String)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "port", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(edu.utah.sci.vistrails.basic:Integer)", 
      "allowedTypes": [
       "o(edu.utah.sci.vistrails.basic:Integer)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "user", 
     "offsetPosition": {
      "top": -15, 
      "left": 160.0
     }, 
     "ddConfig": {
      "type": "i(edu.utah.sci.vistrails.basic:String)", 
      "allowedTypes": [
       "o(edu.utah.sci.vistrails.basic:String)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "password", 
     "offsetPosition": {
      "top": -15, 
      "left": 213.33333333333334
     }, 
     "ddConfig": {
      "type": "i(edu.utah.sci.vistrails.basic:String)", 
      "allowedTypes": [
       "o(edu.utah.sci.vistrails.basic:String)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "keyCertFile", 
     "offsetPosition": {
      "top": -15, 
      "left": 266.66666666666669
     }, 
     "ddConfig": {
      "type": "i(edu.utah.sci.vistrails.basic:File)", 
      "allowedTypes": [
       "o(edu.utah.sci.vistrails.basic:File)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "keyCertFile", 
     "offsetPosition": {
      "bottom": -15, 
      "left": 160.0
     }, 
     "ddConfig": {
      "type": "o(edu.utah.sci.vistrails.basic:File)", 
      "allowedTypes": [
       "i(edu.utah.sci.vistrails.basic:File)", 
       "i(edu.utah.sci.vistrails.basic:Path)", 
       "i(edu.utah.sci.vistrails.basic:Constant)", 
       "i(edu.utah.sci.vistrails.basic:Module)"
      ]
     }
    }
   ], 
   "vt": {
    "cache": 1, 
    "namespace": "", 
    "version": "0.9.0", 
    "package": "com.kitware.climatepipes.esgf"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "ESGFLogin"
 }, 
 {
  "category": "com-kitware-climatepipes-esgf", 
  "container": {
   "fields": [
    {
     "alias": "", 
     "vtype": "edu.utah.sci.vistrails.basic:String", 
     "type": "string", 
     "inputParams": {
      "required": true, 
      "name": "query", 
      "label": "query"
     }
    }, 
    {
     "alias": "", 
     "vtype": "edu.utah.sci.vistrails.basic:String", 
     "type": "string", 
     "inputParams": {
      "required": true, 
      "name": "url", 
      "label": "url"
     }
    }
   ], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "url", 
     "offsetPosition": {
      "top": -15, 
      "left": 160.0
     }, 
     "ddConfig": {
      "type": "i(edu.utah.sci.vistrails.basic:String)", 
      "allowedTypes": [
       "o(edu.utah.sci.vistrails.basic:String)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "value", 
     "offsetPosition": {
      "bottom": -15, 
      "left": 160.0
     }, 
     "ddConfig": {
      "type": "o(edu.utah.sci.vistrails.basic:List)", 
      "allowedTypes": [
       "i(edu.utah.sci.vistrails.basic:List)", 
       "i(edu.utah.sci.vistrails.basic:Constant)", 
       "i(edu.utah.sci.vistrails.basic:Module)"
      ]
     }
    }
   ], 
   "vt": {
    "cache": 1, 
    "namespace": "", 
    "version": "0.9.0", 
    "package": "com.kitware.climatepipes.esgf"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "ESGFSearch"
 }
];