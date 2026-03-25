#!/usr/bin/node

const redheader = document.querySelector("#red_header")
redheader.addEventListener('click', function() {
    document.querySelector("header").style.color = '#FF0000'
});