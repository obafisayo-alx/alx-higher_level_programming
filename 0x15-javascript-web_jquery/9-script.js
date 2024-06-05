#!/usr/bin/node
$.get("https://hellosalut.stefanbohacek.dev/?lang=en",
    function (data) {
        $("#hello").text(data.hello);
    }
);
