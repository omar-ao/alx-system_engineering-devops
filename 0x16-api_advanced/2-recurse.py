#!/usr/bin/python3
"""This is 2-recurse module"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
        queries the Reddit API and returns a list containing
        the titles of all hot articles for a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {"User-Agent": "Python script (by/Omar"}
    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return None
    posts = r.json().get('data')
    for post in posts.get('children'):
        hot_list.append(post.get('data').get('title'))
    after = posts.get('after')
    if after:
        recurse(subreddit, hot_list, after)
    return hot_list
