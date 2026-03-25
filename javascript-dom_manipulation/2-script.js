#!/usr/bin/node

ad = document.querySelector("#red_header")
hd = document.querySelector("header")
ad.addEventListener('click', function() {
    hd.classList.add("red")
})