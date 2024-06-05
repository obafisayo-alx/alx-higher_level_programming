#!/usr/bin/node
$("#update_header").click(function (e) { 
    e.preventDefault();
    $("header").text("New Header!!!");
});
