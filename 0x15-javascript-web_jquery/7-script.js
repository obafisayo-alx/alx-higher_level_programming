#!/usr/bin/node
$.getJSON("https://swapi-api.alx-tools.com/api/people/5/?format=json",
    function (data) {
        $("#character").text(data.name);
        console.log(data.name)
    }
);
