<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="css/main.css" />
        <title>ParaView Web Visualization</title>

        <script src="/PWService/js/ParaViewWeb.js" type="text/javascript"></script>

        <script type="text/javascript">

          //-------------------------------------------------------------------
          function drawImage(imageData)
          {
            var canvas = document.getElementById("draw_image");
            var context = canvas.getContext('2d');
            context.drawImage (imageData, 0, 0);
          }

          //-------------------------------------------------------------------
          function show(data)
          {
            alert('DEBUG: showing data');
            
            // This method might not work on IE
            document.getElementById('nativeimage').src = 'data:image/png;base64,' + data;

            // Update the status
            var status = document.getElementById('status');
            status.innerHTML = '';
          }

          //-------------------------------------------------------------------
          function execute()
          {
            alert('Executing workflow');
            var wf = '<%= request.getParameter("wf") %>';
            wf = wf.replace(/END_OF_LINE/g, '\n');

            // Create a paraview proxy
            // Set the web service base URL
            var serverUrl = "<%=request.getScheme()%>://<%=request.getServerName()%>:<%=request.getServerPort()%>/PWService";
            paraview = new Paraview(serverUrl);
            paraview.createSession("Tutorial-Session-1", "Sample code given for tutorial purpose", "default");
            plugin = paraview.getPlugin("cp_plugin");
            plugin.Asyncexecute(function(image){show(image)}, wf);
          }          
        </script>

    </head>
    <body onUnload="paraview.disconnect();" onload="execute()">
      <div>
        <p id="status"">Processing.....</p>
        <image id="nativeimage" />
      </div>
    </body>
</html>
