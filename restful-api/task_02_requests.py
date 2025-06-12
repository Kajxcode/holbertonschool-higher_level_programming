#!/usr/bin/python3
"""this module defines fetch print and save functions"""

import requests
import csv


URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """fetchs anmd prints"""
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code is 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """fetches and saves"""
    response = requests.get(URL)

    if response.status_code is 200:
        posts = response.json()

        filtered_posts = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer =  csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(filtered_posts)
