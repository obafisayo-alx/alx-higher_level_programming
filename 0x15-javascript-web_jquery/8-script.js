#!/usr/bin/node
$.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json",
    function (data, textStatus, jqXHR) {
        $.map(data.results, function (elementOrValue, indexOrKey) {
            $("#list_movies").append('<li>'+elementOrValue.title+'</li>');
            console.log(elementOrValue.title)
        });
    }
);
