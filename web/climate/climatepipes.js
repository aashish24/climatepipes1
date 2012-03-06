var vt_modules = [];

if(typeof cpsimplified_modules == 'object') {
    vt_modules = vt_modules.concat(cpsimplified_modules);
}

if(typeof basic_modules == 'object') {
    vt_modules = vt_modules.concat(basic_modules);
}

if(typeof esgf_modules == 'object') {
    vt_modules = vt_modules.concat(esgf_modules);
}

if(typeof climatepipes_modules == 'object') {
    vt_modules = vt_modules.concat(climatepipes_modules);
}

if(typeof http_modules == 'object') {
    vt_modules = vt_modules.concat(http_modules);
}

function manageError(error) {
    // Some message 
    alert(error);
    return true; // Propagate the error
}

var locationList = ["World", "Asia", "Africa", "North America", "South America", 
                    "Antarctica", "Europe", "Australia",
                    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
                    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
                    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
                    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
                    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"];

var climatePipes = {

  language: {
    
    languageName: "climatePipes",

    // inputEx fields for pipes properties
    propertiesFields: [
      // default fields (the "name" field is required by the WiringEditor)
      {"type": "string", inputParams: {"name": "name", label: "Title", typeInvite: "Enter a title" } },
      {"type": "text", inputParams: {"name": "description", label: "Description", cols: 30} },

      // Additional fields
      {"type": "boolean", inputParams: {"name": "isTest", value: true, label: "Test"}},
      {"type": "select", inputParams: {"name": "category", label: "Category", selectValues: ["Demo", "Test", "Other"]} }
    ],

    layoutOptions : {
      units: [
        { position: 'top', height: 50, body: 'top'},
        { position: 'left', width: 200, resize: true, body: 'left-all', gutter: '5px', collapse: true,
          collapseSize: 25, header: 'Modules', scroll: true, animate: true },
        { position: 'center', body: 'center-all', gutter: '5px' },
        { header:'Results', position: 'right', width: 500, resize: true, body: 'right', gutter: '5px', collapse: true,
          collapseSize: 25, /*header: 'Properties', scroll: true,*/ animate: true }
      ]
    },
    // List of node types definition
    modules: vt_modules,
  },
  /**
   * @method init
   * @static
   */
  init: function() {
    
    // Configure the adapter backend url :
    WireIt.WiringEditor.adapters.JsonRpc.config.url = "../../../editor/backend/php/WiringEditor.php";
    
    this.editor = new climatePipes.WiringEditor(this.language);

    // Open the infos panel
    editor.accordionView.openPanel(2);
  },
  
  /**
   * Execute the module in the "ExecutionFrame" virtual machine
   * @method run
   * @static
   */
  run: function() {
    //TODO: generate layout xml and run paraview plugin
      var jsonObject = this.editor.getValue();
      var workflowxml = json2workflowxml(jsonObject.working).replace(/END_OF_LINE/g,'\n');

      alert(workflowxml);
      var resultsPanel = document.getElementById("right");

      var serverUrl = "/PWService";
      var paraview = new Paraview(serverUrl);
      paraview.errorListener = window;
      paraview.createSession("mysession", "comment", "default");
      var vtPlugin = paraview.getPlugin("vt_plugin");
      // var result = vtPlugin.execute(workflowxml);
      // var resultArr = result.split("\n", 2);
      // if (resultArr[0] == "Content-Type: text/plain") {
      // 	  resultsPanel.innerHTML = resultArr[1];
      // } else if (resultArr[0] == "Content-Type: image/png" || 
      // 		 resultArr[0] == "Content-Type: image/jpg") {
      // 	  resultsPanel.innerHTML = "<img src=\"" + resultArr[1] + "\">";
      // }  
      // paraview.disconnect();

      vtPlugin.Asyncexecute(function(result){
      	  alert("FINISHED!");
       	  var resultArr = result.split("\n", 2);
      	  if (resultArr[0] == "Content-Type: text/plain") {
      	      resultsPanel.innerHTML = resultArr[1];
      	  } else if (resultArr[0] == "Content-Type: image/png" || 
      		     resultArr[0] == "Content-Type: image/jpg") {
      	      resultsPanel.innerHTML = "<img src=\"" + resultArr[1] + "\">";
      	  }
      	  paraview.disconnect();
      }, workflowxml);
  },

  xml: function() {
    myPanel = new YAHOO.widget.Panel("exportWindow", { 
				       width:"1000px",
				       height:"800px",
				       modal: true,
				       fixedcenter: true,  
				       constraintoviewport: true,  
				       close:true,  
				       draggable:true} ); 

    //.replace(/},{/g, "},\n{");
    var jsonObject = this.editor.getValue();
    var workflowxml = json2workflowxml(jsonObject.working);
    var jsonString = YAHOO.lang.JSON.stringify(jsonObject);
    myPanel.setHeader("XML Workflow"); 
    myPanel.setBody( "<div style='overflow:auto;text-align:left;'><pre>" + workflowxml.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/END_OF_LINE/g,'\n') + "</pre></div>" );
    myPanel.setFooter( "<div style='overflow:auto;'>" + jsonString  + "</div>" );
    myPanel.render(document.body);
    myPanel.show();
  }
};

/**
 * The wiring editor is overriden to add a button "RUN" to the control bar
 */
climatePipes.WiringEditor = function(options) {
   climatePipes.WiringEditor.superclass.constructor.call(this, options);
};

YAHOO.lang.extend(climatePipes.WiringEditor, WireIt.WiringEditor, {
   /**
    * Add the "run" button
    */
   renderButtons: function() {
     // render defualt buttons
     // climatePipes.WiringEditor.superclass.renderButtons.call(this);

     // Add the run button to the toolbar
     var toolbar = YAHOO.util.Dom.get('toolbar');
     var runButton = new YAHOO.widget.Button({ label:"Run", id:"WiringEditor-runButton", container: toolbar });
     runButton.on("click", climatePipes.run, climatePipes, true);
     var xmlButton = new YAHOO.widget.Button({ label:"XML", id:"WiringEditor-xmlButton", container: toolbar });
     xmlButton.on("click", climatePipes.xml, climatePipes, true);
   }
});

function json2workflowxml(json) {
    var result = "<workflow id=\"0\" name=\"ClimatePipes\" version=\"1.0.2"
      +"\" vistrail_id=\"\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance"
      +"\" xsi:schemaLocation=\"http://www.vistrails.org/workflow.xsd\">END_OF_LINE";

    var j = 0;
    for(var i = 0; i < json.wires.length; i+=1) {
      var src = json.wires[i].src;
      var tgt = json.wires[i].tgt;
      if(json.modules[src.moduleId].config.sig[src.terminal][0] == 'i') {
	var tmp = src;
	src = tgt;
	tgt = tmp;
      }
      result+="  <connection id=\""+i+"\">END_OF_LINE";
      result+="    <port id=\""+j+"\" moduleId=\""+src.moduleId
	+"\" moduleName=\""+json.modules[src.moduleId].name
	+"\" name=\""+src.terminal+"\" type=\"source"
	+"\" signature=\""+json.modules[src.moduleId].config.sig[src.terminal].substr(1)
	+"\" />END_OF_LINE";
      result+="    <port id=\""+(j+1)+"\" moduleId=\""+tgt.moduleId
	+"\" moduleName=\""+json.modules[tgt.moduleId].name
	+"\" name=\""+tgt.terminal+"\" type=\"destination"
	+"\" signature=\""+json.modules[tgt.moduleId].config.sig[tgt.terminal].substr(1)
	+"\" />END_OF_LINE";
      result+="  </connection>END_OF_LINE";
      j+=2;
    }

    var fid = 0;
    var pid = 0;
    for(var i = 0; i < json.modules.length; i+=1) {
      var con = json.modules[i];
      var pos = con.config.position;
      
      result+="  <module cache=\""+con.config.vt.cache+"\" id=\""+i+"\" name=\""+con.name
	+"\" namespace=\""+con.config.vt.namespace+"\" package=\""+con.config.vt.package
	+"\" version=\""+con.config.vt.version+"\">END_OF_LINE";
      result+="    <location id=\""+i+"\" x=\""+pos[0]
	+"\" y=\"-"+pos[1]+"\" />END_OF_LINE";
      if(con.config.hasOwnProperty('params') && typeof con.config.params != "undefined") {
	  var fkeys = {};
	  for(var key in con.config.params) {
	      if (con.value[key].length > 0) {
		  var lastBraceIdx = key.lastIndexOf("[");
		  if (key.substr(-1) == "]" && lastBraceIdx != -1) {
		      var k = key.substr(0, lastBraceIdx);
		      var a = key.slice(lastBraceIdx+1, -1);
		      var numkey = parseInt(a) + 1;
		      if (k in fkeys) {
			  if (fkeys[k] < numkey) {
			      fkeys[k] = numkey;
			  }
		      } else {
			  fkeys[k] = numkey;
		      }
		  } else {
		      fkeys[key] = 1;
		  }
	      }
	  }
	  for (var k in fkeys) {
	      result+="    <function id=\""+fid+"\" name=\""+k
		  +"\" pos=\""+fid+"\">END_OF_LINE";
	      for (var j=0; j < fkeys[k]; j+=1) {
		  if (fkeys[k] <= 1) {
		      key = k;
		  } else {
		      key = k + "[" + j + "]";
		  }
		  result+="      <parameter alias=\""+con.config.params[key][0]
		      +"\" id=\"" + pid
		      +"\" name=\"&lt;nodescription&gt;\" pos=\"" + j
		      + "\" type=\""+con.config.params[key][1]
		      +"\" val=\""+con.value[key].replace(/&/g, '&amp;')
		      .replace(/</g, '&lt;')
		      .replace(/>/g, '&gt;')
		      .replace(/"/g, '&quot;')+"\" />END_OF_LINE";
		  pid+=1;
	      }
	      result+="    </function>END_OF_LINE";
	      fid+=1;
	  }
      }
	    
	result+="  </module>END_OF_LINE";
    }
    result+="</workflow>END_OF_LINE";
    return result;
}

//our custom container to include extra data in the exported config
climatePipes.Container = function(options, layer) {
   climatePipes.Container.superclass.constructor.call(this, options, layer);
};

YAHOO.extend(climatePipes.Container, WireIt.FormContainer, {

    /**
     * @method setOptions
     */
    setOptions: function(options) {
      climatePipes.Container.superclass.setOptions.call(this, options);
      
      this.options.vt = options.vt; 
    },

	 
    getConfig: function() {
      var obj = climatePipes.Container.superclass.getConfig.call(this);
      obj.sig = {};
      obj.params = {};

      //add signature info
      for(var i in this.options.terminals) {
	obj.sig[this.options.terminals[i].name] = this.options.terminals[i].ddConfig.type;
      }

      //add parameter info
      for(var j in this.options.fields) {
	var field = this.options.fields[j];
	obj.params[field.inputParams.name] = [field.alias, field.vtype];
      }

      //add vistrails info
      obj.vt = this.options.vt;

      return obj;
    }
});