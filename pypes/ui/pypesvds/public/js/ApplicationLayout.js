/** 
 * @projectDescription test
 * The ApplicationLayout module controls the layout of the pypes interface
 * using the YUI Layout widget. This module defines gutter sizes, scrollable
 * portions, the height/wdith of each setion, and whether or not the section
 * is resizable.
 *
 * @author Eric Gaumer egaumer@pypes.org
 * @version 1.0 
 */
YAHOO.namespace("pypes.ui.layout");

YAHOO.pypes.ui.layout.Window = function () {

	Event = YAHOO.util.Event;
	
    return  {
        myPublicProperty: "I'm accessible as YAHOO.myProject.myModule.myPublicProperty.",
		
		/**
         * Returns a function that will return a number one greater than the previous returned value, starting at n.
         * @alias fooBar
         * @alias FOO.Lib.fooBar
         * @param {Object} n    Number to start with. Default is 1.
         * @return {Function} Returns a function that will return a number one greater than the previous returned value.
         */
        init: function () {
    
            Event.onDOMReady(function() { 
                var layout = new YAHOO.widget.Layout({ 
                    units: [ 
                        {position: 'top', height: 62, body: 'top1', gutter: '1px'}, 
                        {position: 'bottom', height: 20, resize: false, body: 'bottom1', gutter: '1px'}, 
                        {position: 'left', width: 180, resize: true, body: 'left1', gutter: '1px', scroll: true},
                        {position: 'right', width: 620, resize: true, body: 'right1', gutter: '1px', scroll: true},
                        {position: 'center', width: 620, resize: true, body: 'center1', gutter: '1px'}
                    ] 
                });

                layout.on('render', function() { 
                    layout.getUnitByPosition('left').on('close', function() { 
                        closeLeft(); 
                    });

                      // TEST CODE
//                    var r = layout.getUnitByPosition('right');
//                    var el = document.getElementById('aashish');
//                    r.body.appendChild(el);
//                    cal = new YAHOO.widget.Calendar(el);
//                    cal.render();
//                    var p = document.createElement('p');
//                    p.nodeValue = 'hello there';
//                    el.appendChild(p);
//                    alert(p);                    
//                    var link = document.createElement('a');
//                    var href = document.createAttribute('href');
//                    href.nodeValue = '/';
//                    link.setAttributeNode(href);
//                    var img = document.createElement('img');
//                    var srcAttr = document.createAttribute("src");
//                    srcAttr.nodeValue = "/images/KrupePypeLogo.png";
//                    img.setAttributeNode(srcAttr);
//                    link.append(img);
//                    var span = document.createElement('span');
//                    span.appendChild(link);
//                    r.body.appendChild(span);
//                    alert('ehh');
                });

                layout.render(); 
                Event.on('tLeft', 'click', function(ev) { 
                    Event.stopEvent(ev); 
                    layout.getUnitByPosition('left').toggle(); 
                });
            }); 
        }
    };

}();
