<?xml version="1.0" encoding="UTF-8"?>
<html>
 <head>
  <title>ClimatePipes</title>
    <link rel="icon" type="image/png" href="/images/favicon.png">
    <link rel="stylesheet" type="text/css" href="/css/toolbar.css">
    <link rel="stylesheet" type="text/css" href="/css/tree.css">
    <link rel="stylesheet" type="text/css" href="/css/layout.css" />
    <link rel="stylesheet" type="text/css" href="/css/WireIt.css" />

    <!-- YUI -->
    <link rel="stylesheet" type="text/css" href="/js/yui-2.6.0/build/reset/reset-min.css" />
    <link rel="stylesheet" type="text/css" href="/js/yui-2.6.0/build/fonts/fonts-min.css" /> 
    <link rel="stylesheet" type="text/css" href="/js/yui-2.6.0/build/menu/assets/skins/sam/menu.css">
    <link rel="stylesheet" type="text/css" href="/js/yui-2.6.0/build/button/assets/skins/sam/button.css" />
    <link rel="stylesheet" type="text/css" href="/js/yui-2.6.0/build/fonts/fonts.css">
    <link rel="stylesheet" type="text/css" href="/js/yui-2.6.0/build/container/assets/skins/sam/container.css">
    <link rel="stylesheet" type="text/css" href="/js/yui-2.6.0/build/assets/skins/sam/resize.css" />
    <style type="text/css">      
      @import "http://serverapi.arcgisonline.com/jsapi/arcgis/2.7/js/dojo/resources/dojo.css";
      @import "http://serverapi.arcgisonline.com/jsapi/arcgis/2.7/js/dojo/dijit/themes/tundra/tundra.css";
      INPUT.hintTextbox { color: #888; } INPUT.hintTextboxActive { color: #000; }
    </style>

    <script type="text/javascript" src="/js/hint-textbox.js"></script>

    <script type="text/javascript">var djConfig = {parseOnLoad: true};</script>
    <script type="text/javascript" src="http://serverapi.arcgisonline.com/jsapi/arcgis/?v=2.7"></script>
    <script type="text/javascript">
      dojo.require("dijit.layout.BorderContainer");
      dojo.require("dijit.layout.ContentPane");
      dojo.require("dijit.form.DateTextBox");
      dojo.require("esri.map");
      var map;
      function init() {
        var initExtent = new esri.geometry.Extent({"xmin":-13618161,"ymin":5892040,"xmax":-13450611,"ymax":5962515,"spatialReference":{"wkid":102100}});
        map = new esri.Map("map",{extent:initExtent});

        //Add world imagery to the map. View the ArcGIS Online site for services http://arcgisonline/home/search.html?t=content&f=typekeywords:service
        var basemap = new esri.layers.ArcGISTiledMapServiceLayer("http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer");
        map.addLayer(basemap);

        var referenceLayer = new esri.layers.ArcGISTiledMapServiceLayer("http://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer");
        map.addLayer(referenceLayer);


        dojo.connect(map, 'onLoad', function(theMap) {
          //resize the map when the browser resizes
          dojo.connect(dijit.byId('map'), 'resize', map,map.resize);
        });        
      }

      dojo.addOnLoad(init);
    </script>

    <script src="http://localhost:8080/PWService/js/ParaViewWeb.js" type="text/javascript"></script>

  </head>
     <body onUnload="finalizeParaview()" style="background-color:#fff; width:100%; height:100%;" class="yui-skin-sam">
        <div id="top1">
            <div style="height:2px;"></div>
            <div id="toolbar">                
            </div>
        </div> 

        <div id="bottom1"> </div> 

        <div id="left1">
            <div id="tree" style="width:97%; padding-left:10px; padding-top:10px; float:right; height:97%; overflow-y:auto;"><p></p></div>
        </div> 

        <div id="center1" style="padding-left:10px; padding-right:10px; padding-top:10px; padding-bottom:10px">
            <p>Search using pipes </p>            
            <div id="wirelayer" style="height:35%; padding-left:10px; padding-right:10px; padding-top:10px; padding-bottom:10px"></div>
            <p>Search using location </p>            
            <div id="maps">
              <div id="map" style="height:40%; padding-left:10px; padding-right:10px; padding-top:10px; padding-bottom:10px"></div>
              <br>
              <form name="query">                
                <input type="text" name="date1" id="date1" value="FROM (MM-DD-YY)" style="width:15%" class="hintTextbox" />
                <input type="text" name="date2" id="date2" value="TO (MM-DD-YY)" style="width:15%" class="hintTextbox" />
                <input type="text" name="bounds" id="bounds" value="REGION (UL-Lat:UL-Lon:LR-Lat:LR:Lon)" style="width:29.5%" class="hintTextbox" />
                <br><br>
                <input type="text" id="search_text_input" name="search_text" style="width:60%" class="hintTextbox" value="Query"/>
                <input type="submit" value="Submit" />
              </form>
            </div>
        </div>

        <div id="right1">
          <div style="padding-left:20px; padding-top:20px; padding-right:20px" id="results">
            <p id="status"></p>
            <br>
            <image id="nativeimage" />
              <div id="test"></div>
          </div>
        </div>
    </body>
</html>

<div id="proxy" class="WireIt-Container" style="opacity:0.4; left:618px; top:184px; visibility:hidden;">
    <div class="WireIt-Container-ddhandle"></div>
    <div class="body">
        <textarea style="text-align:center;width:100%;height:30px; border-top-width;1px; border-right-width:1px; border-bottom-width:1px; border-left-width:1px; border-style:initial; border-color:initial; padding-top:5px; padding:5px; resize:none; overflow:hidden; font-style:italic;">Dragging...</textarea>
    </div>
    <div class="WireIt-Container-resizehandle"></div>
    <div class="WireIt-Container-closebutton"></div>
    <div class="WireIt-Container-configbutton"></div>
 </div>

<script type="text/javascript" src="/js/yui-2.6.0/build/yuiloader/yuiloader-min.js"></script>
<script type="text/javascript" src="/js/yui-2.6.0/build/event/event-min.js"></script>
<script type="text/javascript" src="/js/yui-2.6.0/build/connection/connection-min.js"></script>
<script type="text/javascript" src="/js/yui-2.6.0/build/dom/dom-min.js"></script>
<script type="text/javascript" src="/js/yui-2.6.0/build/treeview/treeview-min.js"></script>
<script type="text/javascript" src="/js/yui-2.6.0/build/element/element-beta-min.js"></script>
<script type="text/javascript" src="/js/yui-2.6.0/build/button/button-min.js"></script>
<script type="text/javascript" src="/js/yui-2.6.0/build/utilities/utilities.js"></script>
<script type="text/javascript" src="/js/yui-2.6.0/build/container/container-min.js"></script>
<script type="text/javascript" src="/js/yui-2.6.0/build/json/json-min.js"></script>
<script type="text/javascript" src="/js/yui-2.6.0/build/yahoo/yahoo-min.js"></script>
<script type="text/javascript" src="/js/yui-2.6.0/build/menu/menu-min.js"></script>
<script type="text/javascript" src="/js/yui-2.6.0/build/calendar/calendar.js"></script>

<script src="/js/yui-2.6.0/build/resize/resize-min.js"></script> 
<script src="/js/yui-2.6.0/build/yahoo-dom-event/yahoo-dom-event.js"></script>
<script src="/js/yui-2.6.0/build/layout/layout-min.js"></script>
<script src="/js/yui-2.6.0/build/dragdrop/dragdrop-min.js"></script>
<!-- http://yui.yahooapis.com/2.6.0/build/ -->
<!-- Excanvas -->
<!--[if IE]><script type="text/javascript" src="/excanvas.js"></script><![endif]-->

<!-- WireIt -->
<script type="text/javascript" src="/js/wireit/WireIt.js"></script>
<script type="text/javascript" src="/js/wireit/CanvasElement.js"></script>
<script type="text/javascript" src="/js/wireit/Wire.js"></script>
<script type="text/javascript" src="/js/wireit/Terminal.js"></script>
<script type="text/javascript" src="/js/wireit/util/DD.js"></script>
<script type="text/javascript" src="/js/wireit/util/DDResize.js"></script>
<script type="text/javascript" src="/js/wireit/Container.js"></script>
<script type="text/javascript" src="/js/wireit/Layer.js"></script>
<script type="text/javascript" src="/js/wireit/LayerMap-beta.js"></script>

<!--script type="text/javascript" src="http://localhost:8080/PWService/js/ParaViewWeb.js"></script-->
<script type="text/javascript" src="/js/ApplicationLayout.js"></script>
<script type="text/javascript" src="/js/ApplicationMain.js"></script>
<script type="text/javascript" src="/js/ApplicationToolbar.js"></script>
<script type="text/javascript" src="/js/ApplicationTree.js"></script>
