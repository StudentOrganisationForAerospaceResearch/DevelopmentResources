$('document').ready(function(){
    $("h1").click(function(e) {
        console.log("update");
        $.ajax({
            type: "POST",
            url: "/",
            data: "",
            success: function(result) {
                console.log(result);
                $('.time').html("Time: " + result.time);
                $('.total-cpu').html("Total CPUs: " + result.total_cpus);
                $('.cpu-usage').html("CPU Usage: " + result.cpu_usage);
                $('.total-ram').html("Total RAM: " + result.total_ram);
                $('.used-ram').html("Used RAM: " + result.used_ram);
            },
            error: function(result) {
                alert('error');
            }
        });
    });
});