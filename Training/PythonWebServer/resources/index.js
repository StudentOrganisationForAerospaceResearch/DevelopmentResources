$(document).ready(function(){
	$("button").click(function(){
    $.post( "webserver.py", function( data ) {
    $("#Time").text(data.substring(10,18));
    $("#totalCPU").text(data.substring(36, 38));
    $("#cpuUsage").text(data.substring(55,60));
    $("#totalRAM").text(data.substring(77,82));
    $("#usedRAM").text(data.substring(98,102));
    });
  });
});
