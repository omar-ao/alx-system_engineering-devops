#!/usr/bin/python3

"""This is `0-subs.py` module. It contains one function
`number_of_subscribers`
"""
import requests


def number_of_subscribers(subreddit):
    """This is a function that  queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Python scribt"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.ok:
        return r.json().get('data').get('subscribers')
    return 0
