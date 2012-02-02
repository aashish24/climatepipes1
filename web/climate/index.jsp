<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

        <script src="/PWService/js/ParaViewWeb.js" type="text/javascript"></script>

        <title>ParaView Web Visualization (Tutorial)</title>
        <link rel="stylesheet" type="text/css" href="css/main.css" />
    </head>
    <body onUnload="paraview.disconnect();">
        <div class="page">
        </div>

        <script type="text/javascript">
            // Set the web service base URL
            var serverUrl = "<%=request.getScheme()%>://<%=request.getServerName()%>:<%=request.getServerPort()%>/PWService";


            // ---------------- Session 1 -------------------


            // Create a paraview proxy
            var paraview = new Paraview(serverUrl);
            paraview.createSession("Tutorial-Session-1", "Sample code given for tutorial purpose", "default");
            plugin = paraview.getPlugin("climatep");
            plugin.setDataURL('http://www.cnn.com');
            var url = plugin.getDataURL();
            console.log('myurl is ' + url);
    </script>
    </body>
</html>
