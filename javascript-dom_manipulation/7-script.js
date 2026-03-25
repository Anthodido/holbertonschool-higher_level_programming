#!/usr/bin/node

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
.then(function(response) {
    return response.json();
})
.then(function(data) {
    console.log(data);
    const ch = document.querySelector("#list_movies");
    ch.textContent = data.name
    data.results.forEach(function(movie) {
        console.log(movie.title);
        const mt = document.createElement("li");
        mt.textContent = movie.title
        ch.appendChild(mt);
    });
})