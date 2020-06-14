setInterval(function () {
    $('#news').load(window.location.href+' #news');
    //$('#news').html("")
    $( "#news" ).fadeIn( 5000 )
}, 120000)