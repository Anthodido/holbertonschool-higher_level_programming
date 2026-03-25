#!/usr/bin/node

document.addEventListener("DOMContentLoaded", function (){
    fetch("https://hellosalut.stefanbohacek.com/?lang=fr")
.then(function(response) {
    return response.json();
})
.then(function(hello) {
    console.log(hello);
    const he = document.querySelector("#hello");
    he.textContent = hello.hello
})
})