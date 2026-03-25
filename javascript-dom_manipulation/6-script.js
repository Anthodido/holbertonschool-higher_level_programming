#!/usr/bin/node

fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
.then(function(response) {
    return response.json();
})
.then(function(data) {
    console.log(data);
    const ch = document.querySelector("#character");
    ch.textContent = data.name
})