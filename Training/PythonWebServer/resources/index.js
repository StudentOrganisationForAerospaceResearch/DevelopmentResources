$(document).ready(function()
{
    $('button').click(function(){
     $("p#pTest").text('test')
     $.post( "webserver.py", function( data ) 
		{
			$("p#cpuCount").text(data.cpuCount);
			$("p#cpuPercent").text(data.cpuPercent);
			$("p#totalRAM").text(data.totalRAM);
			$("p#availRAM").text(data.availRAM);
			$("p#currentTime").text(data.currentTime);
		});
    })
});
