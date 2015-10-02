$(document).ready(function() {
   var clicked = false, clickX, savedLeftBorder;

   $('#scoreboard_table').bind('mousemove', function( event ){
   		clicked && updateScrollPos(event, savedLeftBorder, clickX);
   });
   
   $('#scoreboard_table').bind('mousedown', function( event ){
        clicked = true;
        clickX = currentXMousePosition(event);
        savedLeftBorder = viewportLeftBorder();
   });
   
   $(window).mouseup(function(){
        clicked = false;
        $('html').css('cursor', 'auto');
   });
});
 
function currentXMousePosition(event) {
   return event.pageX;
}

function viewportLeftBorder(){
   return $('#scoreboard_table').scrollLeft();
}

var updateScrollPos = function(event, savedLeftBorder, clickX) {
    $('html').css('cursor', '-moz-grabbing');
    $('#scoreboard_table').scrollLeft(savedLeftBorder + (clickX - currentXMousePosition(event)));
}