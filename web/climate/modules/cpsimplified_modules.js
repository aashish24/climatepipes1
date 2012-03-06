var cpsimplified_modules = [
 {
  "category": "com-kitware-climatepipes-simplified", 
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
    "package": "com.kitware.climatepipes.simplified"
   }, 
   "xtype": "climatePipes.Container", 
   "icon": "wireit/res/icons/application_edit.png"
  }, 
  "name": "Visualize"
 }
];
