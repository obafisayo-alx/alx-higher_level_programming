#!/usr/bin/node
$(document).ready(function () {
    $("#btn_translate").click(function (e) { 
        e.preventDefault();
        let lang = $("#language_code").val();
        let url = `https://hellosalut.stefanbohacek.dev/?lang=${lang || "en"}`
        $.get(url,
            function (data) {
                $("#hello").text(data.hello);
            }
        );
    });
});