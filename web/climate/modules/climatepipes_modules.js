var climatepipes_modules = [
 {
  "category": "org-vistrails-climatepipes", 
  "container": {
   "fields": [
    {
     "alias": "", 
     "vtype": "edu.utah.sci.vistrails.basic:File", 
     "type": "string", 
     "inputParams": {
      "required": true, 
      "name": "data", 
      "label": "data"
     }
    }, 
    {
     "alias": "", 
     "vtype": "edu.utah.sci.vistrails.basic:String", 
     "type": "string", 
     "inputParams": {
      "required": true, 
      "name": "variable", 
      "label": "variable"
     }
    }
   ], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "data", 
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
     "name": "variable", 
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
     "name": "value", 
     "offsetPosition": {
      "bottom": -15, 
      "left": 160.0
     }, 
     "ddConfig": {
      "type": "o(org.vistrails.climatepipes:CDMSVariable)", 
      "allowedTypes": [
       "i(org.vistrails.climatepipes:CDMSVariable)", 
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
  "name": "CDMSVariable"
 }, 
 {
  "category": "org-vistrails-climatepipes", 
  "container": {
   "fields": [], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "image", 
     "offsetPosition": {
      "top": -15, 
      "left": 160.0
     }, 
     "ddConfig": {
      "type": "i(edu.utah.sci.vistrails.basic:Module)", 
      "allowedTypes": [
       "o(edu.utah.sci.vistrails.basic:Module)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "image", 
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
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "CropImage"
 }, 
 {
  "category": "org-vistrails-climatepipes", 
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
      "type": "o(org.vistrails.climatepipes:CDMSVariable)", 
      "allowedTypes": [
       "i(org.vistrails.climatepipes:CDMSVariable)", 
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
  "name": "First"
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
      "name": "contentType", 
      "label": "contentType"
     }
    }
   ], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "value", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(edu.utah.sci.vistrails.basic:Module)", 
      "allowedTypes": [
       "o(edu.utah.sci.vistrails.basic:Module)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "contentType", 
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
  "name": "WebSink"
 }, 
 {
  "category": "org-vistrails-climatepipes", 
  "container": {
   "fields": [], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(org.vistrails.climatepipes:CDMSVariable)", 
      "allowedTypes": [
       "o(org.vistrails.climatepipes:CDMSVariable)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable2", 
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
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "image", 
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
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "vcsBoxfill"
 }, 
 {
  "category": "org-vistrails-climatepipes", 
  "container": {
   "fields": [], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(org.vistrails.climatepipes:CDMSVariable)", 
      "allowedTypes": [
       "o(org.vistrails.climatepipes:CDMSVariable)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable2", 
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
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "image", 
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
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "vcsIsofill"
 }, 
 {
  "category": "org-vistrails-climatepipes", 
  "container": {
   "fields": [], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(org.vistrails.climatepipes:CDMSVariable)", 
      "allowedTypes": [
       "o(org.vistrails.climatepipes:CDMSVariable)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable2", 
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
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "image", 
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
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "vcsIsoline"
 }, 
 {
  "category": "org-vistrails-climatepipes", 
  "container": {
   "fields": [], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(org.vistrails.climatepipes:CDMSVariable)", 
      "allowedTypes": [
       "o(org.vistrails.climatepipes:CDMSVariable)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable2", 
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
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "image", 
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
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "vcsMeshfill"
 }, 
 {
  "category": "org-vistrails-climatepipes", 
  "container": {
   "fields": [], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(org.vistrails.climatepipes:CDMSVariable)", 
      "allowedTypes": [
       "o(org.vistrails.climatepipes:CDMSVariable)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable2", 
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
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "image", 
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
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "vcsOutfill"
 }, 
 {
  "category": "org-vistrails-climatepipes", 
  "container": {
   "fields": [], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(org.vistrails.climatepipes:CDMSVariable)", 
      "allowedTypes": [
       "o(org.vistrails.climatepipes:CDMSVariable)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable2", 
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
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "image", 
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
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "vcsOutline"
 }, 
 {
  "category": "org-vistrails-climatepipes", 
  "container": {
   "fields": [], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(org.vistrails.climatepipes:CDMSVariable)", 
      "allowedTypes": [
       "o(org.vistrails.climatepipes:CDMSVariable)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable2", 
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
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "image", 
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
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "vcsPlot"
 }, 
 {
  "category": "org-vistrails-climatepipes", 
  "container": {
   "fields": [], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(org.vistrails.climatepipes:CDMSVariable)", 
      "allowedTypes": [
       "o(org.vistrails.climatepipes:CDMSVariable)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable2", 
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
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "image", 
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
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "vcsScatter"
 }, 
 {
  "category": "org-vistrails-climatepipes", 
  "container": {
   "fields": [], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(org.vistrails.climatepipes:CDMSVariable)", 
      "allowedTypes": [
       "o(org.vistrails.climatepipes:CDMSVariable)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable2", 
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
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "image", 
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
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "vcsTaylordiagram"
 }, 
 {
  "category": "org-vistrails-climatepipes", 
  "container": {
   "fields": [], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(org.vistrails.climatepipes:CDMSVariable)", 
      "allowedTypes": [
       "o(org.vistrails.climatepipes:CDMSVariable)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable2", 
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
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "image", 
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
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "vcsVector"
 }, 
 {
  "category": "org-vistrails-climatepipes", 
  "container": {
   "fields": [], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(org.vistrails.climatepipes:CDMSVariable)", 
      "allowedTypes": [
       "o(org.vistrails.climatepipes:CDMSVariable)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable2", 
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
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "image", 
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
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "vcsXvsY"
 }, 
 {
  "category": "org-vistrails-climatepipes", 
  "container": {
   "fields": [], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(org.vistrails.climatepipes:CDMSVariable)", 
      "allowedTypes": [
       "o(org.vistrails.climatepipes:CDMSVariable)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable2", 
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
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "image", 
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
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "vcsXyvsy"
 }, 
 {
  "category": "org-vistrails-climatepipes", 
  "container": {
   "fields": [], 
   "terminals": [
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable", 
     "offsetPosition": {
      "top": -15, 
      "left": 106.66666666666667
     }, 
     "ddConfig": {
      "type": "i(org.vistrails.climatepipes:CDMSVariable)", 
      "allowedTypes": [
       "o(org.vistrails.climatepipes:CDMSVariable)"
      ]
     }
    }, 
    {
     "direction": [
      0, 
      -1
     ], 
     "name": "variable2", 
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
    }, 
    {
     "direction": [
      0, 
      1
     ], 
     "name": "image", 
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
    "version": "0.0.1", 
    "package": "org.vistrails.climatepipes"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "vcsYxvsx"
 }
];
