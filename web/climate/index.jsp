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

          // Sample workflow
          var wf = '\<workflow id=\"0\" name=\"untitled\" version=\"1.0.2\" vistrail_id=\"\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.vistrails.org/workflow.xsd\"\>\n \
            \<connection id=\"0\"\>\n \
              \<port id=\"0\" moduleId=\"1\" moduleName=\"HTTPFile\" name=\"file\" signature=\"(edu.utah.sci.vistrails.basic:File)\" type=\"source\" /\>\n \
              \<port id=\"1\" moduleId=\"0\" moduleName=\"vtkUnstructuredGridReader\" name=\"SetFile\" signature=\"(edu.utah.sci.vistrails.basic:File)\" type=\"destination\" /\>\n \
            \</connection\>\n \
            \<connection id=\"33\"\>\n \
              \<port id=\"66\" moduleId=\"8\" moduleName=\"VTKRenderOffscreen\" name=\"image\" signature=\"(edu.utah.sci.vistrails.basic:File)\" type=\"source\" /\>\n \
              \<port id=\"67\" moduleId=\"28\" moduleName=\"FileSink\" name=\"file\" signature=\"(edu.utah.sci.vistrails.basic:File)\" type=\"destination\" /\>\n \
            \</connection\>\n \
            \<connection id=\"2\"\>\n \
              \<port id=\"4\" moduleId=\"0\" moduleName=\"vtkUnstructuredGridReader\" name=\"GetOutputPort0\" signature=\"(edu.utah.sci.vistrails.vtk:vtkAlgorithmOutput)\" type=\"source\" /\>\n \
              \<port id=\"5\" moduleId=\"2\" moduleName=\"vtkDataSetMapper\" name=\"SetInputConnection0\" signature=\"(edu.utah.sci.vistrails.vtk:vtkAlgorithmOutput)\" type=\"destination\" /\>\n \
            \</connection\>\n \
            \<connection id=\"3\"\>\n \
              \<port id=\"6\" moduleId=\"2\" moduleName=\"vtkDataSetMapper\" name=\"self\" signature=\"(edu.utah.sci.vistrails.vtk:vtkDataSetMapper)\" type=\"source\" /\>\n \
              \<port id=\"7\" moduleId=\"3\" moduleName=\"vtkActor\" name=\"SetMapper\" signature=\"(edu.utah.sci.vistrails.vtk:vtkMapper)\" type=\"destination\" /\>\n \
            \</connection\>\n \
            \<connection id=\"4\"\>\n \
              \<port id=\"8\" moduleId=\"3\" moduleName=\"vtkActor\" name=\"self\" signature=\"(edu.utah.sci.vistrails.vtk:vtkActor)\" type=\"source\" /\>\n \
              \<port id=\"9\" moduleId=\"4\" moduleName=\"vtkRenderer\" name=\"AddActor\" signature=\"(edu.utah.sci.vistrails.vtk:vtkProp)\" type=\"destination\" /\>\n \
            \</connection\>\n \
            \<connection id=\"6\"\>\n \
              \<port id=\"12\" moduleId=\"4\" moduleName=\"vtkRenderer\" name=\"self\" signature=\"(edu.utah.sci.vistrails.vtk:vtkRenderer)\" type=\"source\" /\>\n \
              \<port id=\"13\" moduleId=\"8\" moduleName=\"VTKRenderOffscreen\" name=\"renderer\" signature=\"(edu.utah.sci.vistrails.vtk:vtkRenderer)\" type=\"destination\" /\>\n \
            \</connection\>\n \
            \<module cache=\"1\" id=\"0\" name=\"vtkUnstructuredGridReader\" namespace=\"\" package=\"edu.utah.sci.vistrails.vtk\" version=\"0.9.3\"\>\n \
              \<location id=\"14\" x=\"-71.0\" y=\"156.0\" /\>\n \
            \</module\>\n \
            \<module cache=\"1\" id=\"1\" name=\"HTTPFile\" namespace=\"\" package=\"edu.utah.sci.vistrails.http\" version=\"0.9.0\"\>\n \
              \<location id=\"4\" x=\"-68.0\" y=\"277.0\" /\>\n \
              \<function id=\"0\" name=\"url\" pos=\"0\"\>\n \
                \<parameter alias=\"\" id=\"1\" name=\"&lt;no description&gt;\" pos=\"0\" type=\"edu.utah.sci.vistrails.basic:String\" val=\"http://www.vistrails.org/download/download.php?type=DATA&amp;id=spx.vtk\" /\>\n \
              \</function\>\n \
            \</module\>\n \
            \<module cache=\"1\" id=\"2\" name=\"vtkDataSetMapper\" namespace=\"\" package=\"edu.utah.sci.vistrails.vtk\" version=\"0.9.3\"\>\n \
              \<location id=\"9\" x=\"-84.0\" y=\"10.0\" /\>\n \
            \</module\>\n \
            \<module cache=\"1\" id=\"3\" name=\"vtkActor\" namespace=\"\" package=\"edu.utah.sci.vistrails.vtk\" version=\"0.9.3\"\>\n \
              \<location id=\"11\" x=\"-58.0\" y=\"-98.0\" /\>\n \
            \</module\>\n \
            \<module cache=\"1\" id=\"4\" name=\"vtkRenderer\" namespace=\"\" package=\"edu.utah.sci.vistrails.vtk\" version=\"0.9.3\"\>\n \
              \<location id=\"71\" x=\"-175.393036713\" y=\"-142.355337766\" /\>\n \
              \<function id=\"1\" name=\"SetBackgroundWidget\" pos=\"0\"\>\n \
                \<parameter alias=\"\" id=\"3\" name=\"&lt;no description&gt;\" pos=\"0\" type=\"edu.utah.sci.vistrails.basic:Color\" val=\"0.0,0.0,0.0\" /\>\n \
              \</function\>\n \
            \</module\>\n \
            \<module cache=\"1\" id=\"8\" name=\"VTKRenderOffscreen\" namespace=\"\" package=\"edu.utah.sci.vistrails.vtk\" version=\"0.9.3\"\>\n \
              \<location id=\"72\" x=\"-355.359802212\" y=\"127.680631674\" /\>\n \
            \</module\>\n \
            \<module cache=\"1\" id=\"28\" name=\"FileSink\" namespace=\"\" package=\"edu.utah.sci.vistrails.basic\" version=\"1.6\"\>\n \
              \<location id=\"68\" x=\"-326.075397895\" y=\"-272.430735661\" /\>\n \
              \<function id=\"25\" name=\"overwrite\" pos=\"2\"\>\n \
                \<parameter alias=\"\" id=\"30\" name=\"&lt;no description&gt;\" pos=\"0\" type=\"edu.utah.sci.vistrails.basic:Boolean\" val=\"True\" /\>\n \
              \</function\>\n \
              \<function id=\"29\" name=\"outputPath\" pos=\"2\"\>\n \
                \<parameter alias=\"\" id=\"36\" name=\"&lt;no description&gt;\" pos=\"0\" type=\"edu.utah.sci.vistrails.basic:OutputPath\" val=\"/home/aashish/Desktop/foo.png\" /\>\n \
              \</function\>\n \
              \<function id=\"26\" name=\"publishFile\" pos=\"3\"\>\n \
                \<parameter alias=\"\" id=\"31\" name=\"&lt;no description&gt;\" pos=\"0\" type=\"edu.utah.sci.vistrails.basic:Boolean\" val=\"True\" /\>\n \
              \</function\>\n \
            \</module\>\n \
          \</workflow\>';

         // Draw result now
         plugin.Asyncexecute(function(image){show(image)}, wf);
    </script>
    </body>
</html>
