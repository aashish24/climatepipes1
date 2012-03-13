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
    resultmap.innerHTML = '';
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

var listView = {};

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
        { header:'Results', position: 'right', width: 600, resize: true, body: 'right-all', gutter: '5px', collapse: true,
          collapseSize: 25, /*header: 'Properties', scroll: true,*/ animate: true }
      ]
    },
    // List of node types definition
    modules: vt_modules
  },
  /**
   * @method init
   * @static
   */
  init: function() {
    
    // Configure the adapter backend url :
    // we're not using a backend adapter atm, but wireit complains if you don't set this
    WireIt.WiringEditor.adapters.JsonRpc.config.url = "../../../editor/backend/php/WiringEditor.php";
    
    this.editor = new climatePipes.WiringEditor(this.language);

    // add listener for right panel resizing to manually resize maps and data table
    this.editor.layout.getUnitByPosition("right").subscribe("widthChange",  this.resizeMapAndTable);

    // Open the infos panel
    editor.accordionView.openPanel(2);
  },

  resizeMapAndTable: function(event) {
    if(listView.hasOwnProperty('dataTable') && typeof listView.dataTable != "undefined") {
      var diff = event.newValue - listView.dataTable.getTableEl().offsetWidth;

      var urlCol = listView.dataTable.getColumn("url");

      if(listView.defaultUrlWidth == 0)
	listView.defualtUrlWidth = urlCol.getThEl().offsetWidth;

      if(urlCol.getThEl().offsetWidth + diff < listView.defaultUrlWidth)
	urlCol.getThEl().style.width = listView.defaultUrlWidth;
      else
	urlCol.getThEl().style.width = urlCol.getThEl().offsetWidth + diff + "px";
    }

  },
  
  /**
   * Execute the module in the "ExecutionFrame" virtual machine
   * @method run
   * @static
   */
  run: function() {
      var jsonObject = this.editor.getValue();
      var workflowxml = json2workflowxml(jsonObject.working);

      var resultmap = document.getElementById("result-map");
      var resultlist = document.getElementById("result-list");

      // show progress wheel gif
      resultmap.innerHTML = '<div class="busy-wait"></div>';

      var serverUrl = "/PWService";
      var paraview = new Paraview(serverUrl);
      paraview.errorListener = window;
      paraview.createSession("ClimatePipes", "Executing Vistrails Workflow...", "default");
      var vtPlugin = paraview.getPlugin("vt_plugin");
      vtPlugin.Asyncexecute(function(result){
	  resultmap.innerHTML = '';
       	  var resultArr = result.split("\n", 2);
      	  if (resultArr[0] == "Content-Type: text/plain") {
      	      restulmap.innerHTML = resultArr[1];
      	  } else if (resultArr[0] == "Content-Type: image/png" || 
      		     resultArr[0] == "Content-Type: image/jpg") {
	      overlayImage(resultArr[1]);
      	      //resultmap.innerHTML = "<img src=\"" + resultArr[1] + "\">";
      	  } 

      	  if (resultArr[0] == "Content-Type: application/json") {
	      var files = YAHOO.lang.JSON.parse(resultArr[1]);
	      for(var i = 0; i < files.length; ++i) {
		  if(files[i].var.length > 0)
		      files[i].Variable = files[i].var[0].short_name;
		  else
		      files[i].Variable = 'unknown';
		  files[i].Id = i;
		  files[i].Visualize = "Visualize"; //placeholder for the button
	      }
	      resultlist.innerHTML='<div id="listViewTable"></div>';
	      listView.Data = files;
	      BuildDataTable();
	      this.resizeMapAndTable({newValue: this.editor.layout.getUnitByPosition("right").getSizes().body.w});
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
    myPanel.setBody( "<div style='overflow:auto;text-align:left;'><pre>" + workflowxml.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;") + "</pre></div>" );
    myPanel.setFooter( "<div style='overflow:auto;'>" + jsonString  + "</div>" );
    myPanel.render(document.body);
    myPanel.show();
    },

  createVisualizePipeline: function(url, vari) {
	this.clear();

	DataFileConfig.fields[0].inputParams.value = url;
	DataFileConfig.fields[1].inputParams.value = vari;

	this.editor.layer.addContainer(ESGFSourceConfig);
	this.editor.layer.addContainer(DataFileConfig);
	this.editor.layer.addContainer(VisualizeConfig);

	this.editor.layer.addWire(wire0_1_source_source);
	this.editor.layer.addWire(wire1_2_query_query);

	this.run();
    },

  googleMapSubmit: function() {
	//determine which source to use
	var elSource = document.getElementById("selectSource");
	var source = elSource.options[elSource.selectedIndex].text;

	var keywords = document.getElementById("search_text_input").value;
	var from     = document.getElementById("date1").value;
	var to       = document.getElementById("date2").value;
	var location = document.getElementById("bounds").value;
	var numitems = document.getElementById("numitems").value;

	if(keywords == 'Keywords') keywords = '';
	if(from == 'From (mm-dd-yy)') from = '';
	if(to == 'To (mm-dd-yy)') to = '';
	if(location == 'Region (minLat,maxLat,minLng,maxLng)') location = '';
	if(numitems == '# of Items') numitems = 1;

	//determine which view to use
	var elView = document.getElementById("selectView");
	var view = elView.options[elView.selectedIndex].text;

	this.createQueryPipeline(source, keywords, from, to, location, numitems, view);
    },

  createQueryPipeline: function(source, keywords, from, to, location, numitems, view) {
	this.clear();

	QueryConfig.fields[0].inputParams.value = keywords;
	QueryConfig.fields[1].inputParams.value = from;
	QueryConfig.fields[2].inputParams.value = to;
	QueryConfig.fields[3].inputParams.value = location;
	QueryConfig.fields[4].inputParams.value = numitems;

	switch(source) {
	case 'KitwareSource': //TODO: add kitware source once we have one
	case 'ESGFSource': this.editor.layer.addContainer(ESGFSourceConfig); break;
	default: this.editor.layer.addContainer(ESGFSourceConfig); break;
	}

	this.editor.layer.addContainer(QueryConfig);

	switch(view) {
	case 'ListData': this.editor.layer.addContainer(ListDataConfig); break;
	case 'Visualize': this.editor.layer.addContainer(VisualizeConfig); break;
	default: this.editor.layer.addContainer(ListDataConfig); break;
	}

	this.editor.layer.addWire(wire0_1_source_source);
	this.editor.layer.addWire(wire1_2_query_query);

	this.run();
    },

  clear: function() {
	this.editor.layer.clear();
    },

  testing: function() {
    /* Testing module and wire creation */
    // var modules = VisualizePipelineConfig.containers;
    // modules[1].fields[0].inputParams.value = 'someurl';
    // modules[1].fields[1].inputParams.value = 'somevarname';
    // var wires = VisualizePipelineConfig.wires;
    // for(var i in modules)
    //     this.editor.layer.addContainer(modules[i]);
    // for(var j in wires)
    //     this.editor.layer.addWire(wires[j]);


    /* Testing List View */
    var resultsPanel = document.getElementById("result-list");
    resultsPanel.innerHTML='<div id="listViewTable"></div>';
    var testData =
      {'url':'http://www.google.com/somereallylongfilenamefile.nc', 
       'var':[{'rank':1.0,'name':'North Atlantic Draft','short_name':'nad'}, 
	      {'rank':1.2,'name':'South Atlantic Draft','short_name':'sad'}],
       'rank': 1.5, 
       'Variable':'nad', 
       'Id':0,
       'Visualize':'Visualize',
       'randomotherthing':'withval'};

    listView.Data = [];
    for(var i = 0; i < 25; i++)
      listView.Data.push(testData);

    listView.varOptions = [[{label:'Lable1', value:'val1'},
			    {label:'Lable2', value:'val2'},
			    {label:'Lable3', value:'val3'}]];
    BuildDataTable();	      
    this.resizeMapAndTable({newValue: this.editor.layout.getUnitByPosition("right").getSizes().body.w});
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
     var clrButton = new YAHOO.widget.Button({ label:"Clear", id:"WiringEditor-clrButton", container: toolbar });
     clrButton.on("click", climatePipes.clear, climatePipes, true);
     // var tstButton = new YAHOO.widget.Button({ label:"TestPipelineCreation", id:"WiringEditor-tstButton", container: toolbar });
     // tstButton.on("click", climatePipes.testing, climatePipes, true);
   }
});


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
      obj.fields = [];
      obj.terminals = this.options.terminals;

      //add signature info
      for(var i in this.options.terminals) {
	obj.sig[this.options.terminals[i].name] = this.options.terminals[i].ddConfig.type;
      }

      //add parameter info
      for(var j in this.options.fields) {
	var field = this.options.fields[j];
	obj.params[field.inputParams.name] = [field.alias, field.vtype];
	obj.fields.push(field);
	obj.fields[j].inputParams.container = null; // prevent infinite loop
      }

      //add vistrails info
      obj.vt = this.options.vt;

      return obj;
    }
});

var resultMap;

function initResultMap()
{
  var latlng = new google.maps.LatLng(43, -89);
  var settings = {
      zoom: 4,
      center: latlng,
      mapTypeControl: true,
      mapTypeControlOptions: {
          style: google.maps.MapTypeControlStyle.DROPDOWN_MENU
      },
      navigationControl: true,
      navigationControlOptions: {
          style: google.maps.NavigationControlStyle.SMALL
      },
      mapTypeId: google.maps.MapTypeId.SATELLITE
  };

  var resultMapElem = $("#result-map");
  //document.getElementById("result-map").style.height='100%';
  //document.getElementById("result-map").style.width='100%';
  resultMap = new google.maps.Map(resultMapElem[0], settings);
}


function overlayImage( filename )
{
  alert(window.location.pathname.split( '/' ));

  initResultMap();

  // \NOTE Hard coded bounds for now
  var imageBounds = new google.maps.LatLngBounds(
      new google.maps.LatLng(-89.9999,-179.9999),
      new google.maps.LatLng( 89.9999, 179.9999));

  // \NOTE Hard coded base URL for now
  var imageUrl =  'http://localhost:8080' + '/' + filename;
  // \TODO Remove later
  alert( imageUrl );
  var myOverlay = new google.maps.GroundOverlay( filename, imageBounds );
  myOverlay.setMap( resultMap );
}

// YUI DataTable definition
function BuildDataTable() {
    // Define a custom formatter for the cdms variable column
    listView.variableDropdown = function(elLiner, oRecord, oColumn, oData) {
	var idx = oRecord.getData("Id");
	var opts = [];
	
	// create dropdown options from cdms variables
	for(var j=0; j<listView.Data[idx].var.length; j++) {
	    var option ={"value":listView.Data[idx].var[j].short_name,
			 "label":listView.Data[idx].var[j].name}; 
	    opts.push(option);
	}
	
	if(opts.length > 0) {
	    oColumn.dropdownOptions = opts;
	    YAHOO.widget.DataTable.formatDropdown(elLiner, oRecord, oColumn, oData);
	} else {
	    elLiner.innerHTML = 'unknown'; //only get here if file had no variables
	}
    };
        
    // Add the custom formatter to the shortcuts
    YAHOO.widget.DataTable.Formatter.variableDD = listView.variableDropdown;

    // Override the built-in link formatter to just show the filename
    YAHOO.widget.DataTable.formatLink = function(elLiner, oRecord, oColumn, oData) {
	elLiner.innerHTML = '<a href="' + oData + '">' + oData.replace(/^.*[\\\/]/, '') + '</a>';
    };

    var columnDefs = 
	[{key:"Id", formatter:"number", resizeable:true},
	 {key:"url", label: "Filename", formatter:YAHOO.widget.DataTable.formatLink, resizeable:true},
	 {key:"Variable", formatter:"variableDD", resizeable:true},
	 {key:"Visualize", formatter:YAHOO.widget.DataTable.formatButton, resizeable:true}];

    listView.dataSource = new YAHOO.util.DataSource(listView.Data);
    listView.dataSource.responseType = YAHOO.util.DataSource.TYPE_JSARRAY;
    listView.dataSource.responseSchema = {
	fields: ['Id', 'url', 'Variable', 'Visualize']
    };

    listView.dataTable = new YAHOO.widget.DataTable("listViewTable", columnDefs, listView.dataSource);
	
    listView.dataTable.subscribe("buttonClickEvent", function(oArgs) {
	    var oRec = this.getRecord(oArgs.target);
	    var url = oRec.getData("url");
	    var vari = oRec.getData("Variable");
	    climatePipes.createVisualizePipeline(url, vari);
	});

    var variableDropDownChanged = function(evt) {
	var tar = YAHOO.util.Event.getTarget(evt);
	var oRec = listView.dataTable.getRecord(tar);
	oRec.setData("Variable", tar.value);
    };

    // add a listener to drop down changed on table
    YAHOO.util.Event.delegate(listView.dataTable.getTbodyEl(), "change", variableDropDownChanged, "select");

  listView.defaultUrlWidth = 0;
};

var ESGFSourceConfig = {"fields":[{"alias":"","vtype":"edu.utah.sci.vistrails.basic:String","type":"string","inputParams":{"required":true,"name":"host","label":"host"}},{"alias":"","vtype":"edu.utah.sci.vistrails.basic:Integer","type":"string","inputParams":{"required":true,"name":"port","label":"port"}},{"alias":"","vtype":"edu.utah.sci.vistrails.basic:String","type":"string","inputParams":{"required":true,"name":"user","label":"user"}},{"alias":"","vtype":"edu.utah.sci.vistrails.basic:String","type":"string","inputParams":{"required":true,"name":"password","label":"password"}}],"terminals":[{"direction":[0,-1],"name":"host","offsetPosition":{"top":-15,"left":64},"ddConfig":{"type":"i(edu.utah.sci.vistrails.basic:String)","allowedTypes":["o(edu.utah.sci.vistrails.basic:String)"]}},{"direction":[0,-1],"name":"port","offsetPosition":{"top":-15,"left":128},"ddConfig":{"type":"i(edu.utah.sci.vistrails.basic:Integer)","allowedTypes":["o(edu.utah.sci.vistrails.basic:Integer)"]}},{"direction":[0,-1],"name":"user","offsetPosition":{"top":-15,"left":192},"ddConfig":{"type":"i(edu.utah.sci.vistrails.basic:String)","allowedTypes":["o(edu.utah.sci.vistrails.basic:String)"]}},{"direction":[0,-1],"name":"password","offsetPosition":{"top":-15,"left":256},"ddConfig":{"type":"i(edu.utah.sci.vistrails.basic:String)","allowedTypes":["o(edu.utah.sci.vistrails.basic:String)"]}},{"direction":[0,1],"name":"source","offsetPosition":{"bottom":-15,"left":160},"ddConfig":{"type":"o(org.vistrails.climatepipes:cpSource)","allowedTypes":["i(org.vistrails.climatepipes:cpSource)","i(edu.utah.sci.vistrails.basic:Module)"]}}],"vt":{"cache":1,"namespace":"","version":"0.0.1","package":"org.vistrails.climatepipes"},"xtype":"climatePipes.Container","icon":"wireit/res/icons/application_edit.png","position":[20,20],"title":"ESGFSource"};

var QueryConfig = {"fields":[{"alias":"","vtype":"edu.utah.sci.vistrails.basic:String","type":"string","inputParams":{"required":true,"name":"Keywords","label":"Keywords"}},{"alias":"","vtype":"edu.utah.sci.vistrails.basic:String","type":"string","inputParams":{"required":true,"name":"From","label":"From"}},{"alias":"","vtype":"edu.utah.sci.vistrails.basic:String","type":"string","inputParams":{"required":true,"name":"To","label":"To"}},{"alias":"","vtype":"edu.utah.sci.vistrails.basic:String","type":"string","inputParams":{"required":true,"name":"Location","label":"Location"}},{"alias":"","vtype":"edu.utah.sci.vistrails.basic:Integer","type":"string","inputParams":{"required":true,"name":"numitems","label":"numitems"}}],"terminals":[{"direction":[0,-1],"name":"source","offsetPosition":{"top":-15,"left":45.714285714285715},"ddConfig":{"type":"i(org.vistrails.climatepipes:cpSource)","allowedTypes":["o(org.vistrails.climatepipes:cpSource)"]}},{"direction":[0,-1],"name":"Keywords","offsetPosition":{"top":-15,"left":91.42857142857143},"ddConfig":{"type":"i(edu.utah.sci.vistrails.basic:String)","allowedTypes":["o(edu.utah.sci.vistrails.basic:String)"]}},{"direction":[0,-1],"name":"From","offsetPosition":{"top":-15,"left":137.14285714285714},"ddConfig":{"type":"i(edu.utah.sci.vistrails.basic:String)","allowedTypes":["o(edu.utah.sci.vistrails.basic:String)"]}},{"direction":[0,-1],"name":"To","offsetPosition":{"top":-15,"left":182.85714285714286},"ddConfig":{"type":"i(edu.utah.sci.vistrails.basic:String)","allowedTypes":["o(edu.utah.sci.vistrails.basic:String)"]}},{"direction":[0,-1],"name":"Location","offsetPosition":{"top":-15,"left":228.57142857142858},"ddConfig":{"type":"i(edu.utah.sci.vistrails.basic:String)","allowedTypes":["o(edu.utah.sci.vistrails.basic:String)"]}},{"direction":[0,-1],"name":"numitems","offsetPosition":{"top":-15,"left":274.2857142857143},"ddConfig":{"type":"i(edu.utah.sci.vistrails.basic:Integer)","allowedTypes":["o(edu.utah.sci.vistrails.basic:Integer)"]}},{"direction":[0,1],"name":"query","offsetPosition":{"bottom":-15,"left":160},"ddConfig":{"type":"o(org.vistrails.climatepipes:cpQuery)","allowedTypes":["i(org.vistrails.climatepipes:cpQuery)","i(edu.utah.sci.vistrails.basic:Module)"]}}],"vt":{"cache":1,"namespace":"","version":"0.0.1","package":"org.vistrails.climatepipes"},"xtype":"climatePipes.Container","icon":"wireit/res/icons/application_edit.png","position":[203,177],"title":"Query"};

var DataFileConfig = {"fields":[{"alias":"","vtype":"edu.utah.sci.vistrails.basic:String","type":"string","inputParams":{"required":true,"name":"url","label":"url"}},{"alias":"","vtype":"edu.utah.sci.vistrails.basic:String","type":"string","inputParams":{"required":true,"name":"variable","label":"variable"}}],"terminals":[{"direction":[0,-1],"name":"source","offsetPosition":{"top":-15,"left":80},"ddConfig":{"type":"i(org.vistrails.climatepipes:cpSource)","allowedTypes":["o(org.vistrails.climatepipes:cpSource)"]}},{"direction":[0,-1],"name":"url","offsetPosition":{"top":-15,"left":160},"ddConfig":{"type":"i(edu.utah.sci.vistrails.basic:String)","allowedTypes":["o(edu.utah.sci.vistrails.basic:String)"]}},{"direction":[0,-1],"name":"variable","offsetPosition":{"top":-15,"left":240},"ddConfig":{"type":"i(edu.utah.sci.vistrails.basic:String)","allowedTypes":["o(edu.utah.sci.vistrails.basic:String)"]}},{"direction":[0,1],"name":"query","offsetPosition":{"bottom":-15,"left":160},"ddConfig":{"type":"o(org.vistrails.climatepipes:cpQuery)","allowedTypes":["i(org.vistrails.climatepipes:cpQuery)","i(edu.utah.sci.vistrails.basic:Module)"]}}],"vt":{"cache":1,"namespace":"","version":"0.0.1","package":"org.vistrails.climatepipes"},"xtype":"climatePipes.Container","icon":"wireit/res/icons/application_edit.png","position":[125,163],"title":"DataFile"};

var VisualizeConfig = {"fields":[],"terminals":[{"direction":[0,-1],"name":"query","offsetPosition":{"top":-15,"left":160},"ddConfig":{"type":"i(org.vistrails.climatepipes:cpQuery)","allowedTypes":["o(org.vistrails.climatepipes:cpQuery)"]}}],"vt":{"cache":1,"namespace":"","version":"0.0.1","package":"org.vistrails.climatepipes.simplified"},"xtype":"climatePipes.Container","icon":"wireit/res/icons/application_edit.png","position":[248,270],"title":"Visualize"};

var ListDataConfig = {"fields":[],"terminals":[{"direction":[0,-1],"name":"query","offsetPosition":{"top":-15,"left":160},"ddConfig":{"type":"i(org.vistrails.climatepipes:cpQuery)","allowedTypes":["o(org.vistrails.climatepipes:cpQuery)"]}}],"vt":{"cache":1,"namespace":"","version":"0.0.1","package":"org.vistrails.climatepipes.simplified"},"xtype":"climatePipes.Container","icon":"wireit/res/icons/application_edit.png","position":[400,350],"title":"ListData"};

var wire0_1_source_source = {"src":{"moduleId":0,"terminal":"source"},"tgt":{"moduleId":1,"terminal":"source"}};

var wire1_2_query_query = {"src":{"moduleId":1,"terminal":"query"},"tgt":{"moduleId":2,"terminal":"query"}};

function json2workflowxml(json, newLine, indent) {
    // default params
    newLine = typeof newLine !== 'undefined' ? newLine : '\n';
    indent = typeof indent !== 'undefined' ? indent : '  ';

    var result = "<workflow id=\"0\" name=\"ClimatePipes\" version=\"1.0.2"
      +"\" vistrail_id=\"\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance"
      +"\" xsi:schemaLocation=\"http://www.vistrails.org/workflow.xsd\">" + newLine;

    var j = 0;
    for(var i = 0; i < json.wires.length; i+=1) {
      var src = json.wires[i].src;
      var tgt = json.wires[i].tgt;
      if(json.modules[src.moduleId].config.sig[src.terminal][0] == 'i') {
	var tmp = src;
	src = tgt;
	tgt = tmp;
      }
      result+=indent+"<connection id=\""+i+"\">" + newLine;
      result+=indent+indent+"<port id=\""+j+"\" moduleId=\""+src.moduleId
	+"\" moduleName=\""+json.modules[src.moduleId].name
	+"\" name=\""+src.terminal+"\" type=\"source"
	+"\" signature=\""+json.modules[src.moduleId].config.sig[src.terminal].substr(1)
	+"\" />" + newLine;
      result+=indent+indent+"<port id=\""+(j+1)+"\" moduleId=\""+tgt.moduleId
	+"\" moduleName=\""+json.modules[tgt.moduleId].name
	+"\" name=\""+tgt.terminal+"\" type=\"destination"
	+"\" signature=\""+json.modules[tgt.moduleId].config.sig[tgt.terminal].substr(1)
	+"\" />" + newLine;
      result+=indent+"</connection>" + newLine;
      j+=2;
    }

    var fid = 0;
    var pid = 0;
    for(var i = 0; i < json.modules.length; i+=1) {
      var con = json.modules[i];
      var pos = con.config.position;
      
      result+=indent+"<module cache=\""+con.config.vt.cache+"\" id=\""+i+"\" name=\""+con.name
	+"\" namespace=\""+con.config.vt.namespace+"\" package=\""+con.config.vt.package
	+"\" version=\""+con.config.vt.version+"\">" + newLine;
      result+=indent+indent+"<location id=\""+i+"\" x=\""+pos[0]
	+"\" y=\"-"+pos[1]+"\" />" + newLine;
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
	      result+=indent+indent+"<function id=\""+fid+"\" name=\""+k
		  +"\" pos=\""+fid+"\">" + newLine;
	      for (var j=0; j < fkeys[k]; j+=1) {
		  if (fkeys[k] <= 1) {
		      key = k;
		  } else {
		      key = k + "[" + j + "]";
		  }
		  result+=indent+indent+indent+"<parameter alias=\""+con.config.params[key][0]
		      +"\" id=\"" + pid
		      +"\" name=\"&lt;nodescription&gt;\" pos=\"" + j
		      + "\" type=\""+con.config.params[key][1]
		      +"\" val=\""+con.value[key].replace(/&/g, '&amp;')
		      .replace(/</g, '&lt;')
		      .replace(/>/g, '&gt;')
		      .replace(/"/g, '&quot;')+"\" />" + newLine;
		  pid+=1;
	      }
	      result+=indent+indent+"</function>" + newLine;
	      fid+=1;
	  }
      }
	    
	result+=indent+"</module>" + newLine;
    }
    result+="</workflow>" + newLine;
    return result;
}
