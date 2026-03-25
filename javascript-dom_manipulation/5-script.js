#!/usr/bin/node

const upheader = document.querySelector("#update_header")
upheader.addEventListener('click', function() {
    he = document.querySelector("header")
    he.textContent = "New Header!!!"
});