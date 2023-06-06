#!/usr/bin/python3
""" Write a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
    for a given subreddit."""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {"User-Agent": "MyApp/1.0"}

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        data = data.get("data").get("children")
        for items in data:
            print(items.get('data').get('title'))
    else:
        print(None)
    return 0
