#!/usr/bin/python3

"""This is `0-subs.py` module. It contains one function
`number_of_subscribers"""
import requests


def number_of_subscribers(subreddit):
    """This is a function that  queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url)
    if r.status_code != 200:
        return 0
    return r.json()['data']['subscribers']
