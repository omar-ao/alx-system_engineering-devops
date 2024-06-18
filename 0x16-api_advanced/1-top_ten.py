#!/usr/bin/python3
"""This module contains one function: top_ten"""
import requests


def top_ten(subreddit):
    """This function queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Pyton script"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if not r.ok:
        return 0
    children = r.json().get('data').get('children')
    for child in children:
        post = child['data']
        print(post['title'])
