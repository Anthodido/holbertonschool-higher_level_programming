#!/usr/bin/python3

import requests
import csv
URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():

    reponse = requests.get(URL)
    print(f"Status Code: {reponse.status_code}")
    if reponse.status_code == 200 :
        data = reponse.json()
        for post in data:
            print(post["title"])

def fetch_and_save_posts():

    reponse = requests.get(URL)
    print(f"Status Code: {reponse.status_code}")
    if reponse.status_code == 200 :
        data = reponse.json()
        rows = []
        for post in data:
            rows.append({"id": post["id"], "title": post["title"], "body": post["body"]})
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(rows)
