<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="css/main.css" />
        <title>ParaView Web Visualization</title>

        <script src="/PWService/js/ParaViewWeb.js" type="text/javascript"></script>

        <script type="text/javascript">
          function drawImage(imageData)
          {
            var canvas = document.getElementById("draw_image");
            var context = canvas.getContext('2d');
            context.drawImage (imageData, 0, 0);
          }

          String.prototype.padRight = function(c, n)
          {
            var txt = '';
            for(var i=0;i<n-this.length;i++) txt += c;
            return txt + this;
          };

          function show(data)
          {
            // This method might not work on IE
            document.getElementById('nativeimage').src = 'data:image/png;base64,' + data;
          }

        </script>

    </head>

    <body onUnload="paraview.disconnect();">
        <div id="page"></div>
        <div id="test"></div>
        <div id="image"></div>
        <div id="largeimage"></div>
        <img id="nativeimage" />

        <script type="text/javascript">
            // Set the web service base URL
            var serverUrl = "<%=request.getScheme()%>://<%=request.getServerName()%>:<%=request.getServerPort()%>/PWService";

            document.getElementById("test").innerHTML = 'hi'


            // Create a paraview proxy
            paraview = new Paraview(serverUrl);
            paraview.createSession("Tutorial-Session-1", "Sample code given for tutorial purpose", "default");
            plugin = paraview.getPlugin("cp_plugin");

            //plugin.setDataURL('http://www.cnn.com');
            //var url = plugin.getDataURL();
            //console.log('myurl is ' + url);

            //var result = plugin.execute('hello world');
            //document.getElementById("page").innerHTML = result.data;

            // Draw image now
           //show(plugin.testGetImageBinaryData());
            show(plugin.execute('/home/aashish/Desktop/test2.xml'))
    </script>
    </body>
</html>
