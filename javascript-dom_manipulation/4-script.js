#!/usr/bin/node

ad = document.querySelector("#add_item")
ml = document.querySelector(".my_list")
ad.addEventListener('click', function() {
    const new_item = document.createElement("li");
    new_item.textContent = "Item"
    ml.appendChild(new_item);
})