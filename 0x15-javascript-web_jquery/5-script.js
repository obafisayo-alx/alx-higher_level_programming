#!/usr/bin/node
$("#add_item").click(function (e) { 
    e.preventDefault();
    $(".my_list").append("<li>Item</li>");
});
