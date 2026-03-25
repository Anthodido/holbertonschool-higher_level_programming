#!/usr/bin/node

ad = document.querySelector("#toggle_header")
hd = document.querySelector("header")
ad.addEventListener('click', function() {
    hd.classList.toggle("red")
    hd.classList.toggle("green")
})