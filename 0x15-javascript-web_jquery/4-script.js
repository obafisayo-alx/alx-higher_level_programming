#!/usr/bin/node
$("#toggle_header").click(function (e) { 
    e.preventDefault();
    if ($('header').hasClass('green')) {
        $('header').removeClass('green');
        $('header').addClass('red');
    } else if ($('header').hasClass('red')) {
        $('header').removeClass('red');
        $('header').addClass('green');
    }
});
