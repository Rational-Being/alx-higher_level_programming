$(function () {
    const apiUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json";
    $.get(apiUrl, function (data) {
        data.results.forEach(function (tittles) {
            $("<li>").text(tittles.tittle).appendTo('ul#list_movies');
        }
            
        });
    });
});