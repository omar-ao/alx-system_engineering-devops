#!/usr/bin/python3
"""This is 100-count module, It contains
one function:- count_words"""
import requests


def count_words(subreddit, word_list, count={}, after=''):
    """
        queries the Reddit API, parses the title of all hot articles
        and prints a sorted count of given keywords (case-insensitive
        delimited by spaces.
    """
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {"User-Agent": "script (by/Omar"}
    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return None
    if not count:
        count = {key.lower(): 0 for key in word_list}
    value = r.json().get("data")
    for post in value.get("children"):
        for title in post.get("data").get("title").split():
            for key in count:
                if title.lower() == key:
                    count[key] += 1
    after = value.get("after")
    if after:
        count_words(subreddit, word_list, count, after)
    else:
        count = dict(sorted(count.items()))
        count = dict(sorted(count.items(), key=lambda item: item[1],
                            reverse=True))
        for key in count:
            if count[key] != 0:
                print("{}: {}".format(key, count[key]))
