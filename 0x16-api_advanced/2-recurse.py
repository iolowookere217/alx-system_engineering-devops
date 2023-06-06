#!/usr/bin/python3
""" Write a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
    for a given subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json?after={}".\
           format(subreddit, after)
    header = {"User-Agent": "MyApp/1.0"}

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        after = data.get("data").get("after")
        children_list = data.get("data").get("children")
        for items in children_list:
            hot_list.append(items.get('data').get('title'))
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
