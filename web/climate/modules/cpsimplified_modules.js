var cpsimplified_modules = [

 {
  "category": "org-vistrails-climatepipes", 
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
     "name": "source", 
     "offsetPosition": {
      "bottom": -15, 
      "left": 160.0
     }, 
     "ddConfig": {
      "type": "o(org.vistrails.climatepipes:cpSource)", 
      "allowedTypes": [
       "i(org.vistrails.climatepipes:cpSource)", 
       "i(edu.utah.sci.vistrails.basic:Module)"
      ]
     }
    }
   ], 
   "vt": {
    "cache": 1, 
    "namespace": "", 
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "ESGFSource"
 },
 {
  "category": "org-vistrails-climatepipes", 
  "container": {
   "fields": [
    {
     "alias": "", 
     "vtype": "edu.utah.sci.vistrails.basic:String", 
     "type": "string", 
     "inputParams": {
      "required": true, 
      "name": "keywords", 
      "label": "keywords"
     }
    }, 
    {
     "alias": "", 
     "vtype": "edu.utah.sci.vistrails.basic:Integer", 
     "type": "string", 
     "inputParams": {
      "required": true, 
      "name": "numitems", 
      "label": "numitems"
     }
    }
   ], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "source", 
     "offsetPosition": {
      "top": -15, 
      "left": 80.0
     }, 
     "ddConfig": {
      "type": "i(org.vistrails.climatepipes:cpSource)", 
      "allowedTypes": [
       "o(org.vistrails.climatepipes:cpSource)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "keywords", 
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
     "name": "numitems", 
     "offsetPosition": {
      "top": -15, 
      "left": 240.0
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
      1
     ], 
     "name": "data", 
     "offsetPosition": {
      "bottom": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "o(edu.utah.sci.vistrails.basic:List)", 
      "allowedTypes": [
       "i(edu.utah.sci.vistrails.basic:List)", 
       "i(edu.utah.sci.vistrails.basic:Constant)", 
       "i(edu.utah.sci.vistrails.basic:Module)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "files", 
     "offsetPosition": {
      "bottom": -15, 
      "left": 213.33333333333334
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
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "Query"
 },
 {
  "category": "org-vistrails-climatepipes-simplified", 
  "container": {
   "fields": [
    {
     "alias": "", 
     "vtype": "edu.utah.sci.vistrails.basic:List", 
     "type": "string", 
     "inputParams": {
      "required": true, 
      "name": "list", 
      "label": "list"
     }
    }
   ], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "list", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(edu.utah.sci.vistrails.basic:List)", 
      "allowedTypes": [
       "o(edu.utah.sci.vistrails.basic:List)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "var", 
     "offsetPosition": {
      "top": -15, 
      "left": 213.33333333333334
     }, 
     "ddConfig": {
      "type": "i(org.vistrails.climatepipes:CDMSVariable)", 
      "allowedTypes": [
       "o(org.vistrails.climatepipes:CDMSVariable)"
      ]
     }
    }
   ], 
   "vt": {
    "cache": 1, 
    "namespace": "", 
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes.simplified"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "Visualize"
 }
];
