#!/usr/bin/node
$("#red_header").click(function (e) { 
    e.preventDefault();
    $("header").addClass("red");
});
