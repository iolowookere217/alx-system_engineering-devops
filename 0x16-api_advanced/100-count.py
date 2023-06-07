#!/usr/bin/python3
"""a recursive function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces"""

import requests


def count_words(subreddit, word_list, my_dict={}, after=None):
    url = "https://www.reddit.com/r/{}/hot/.json?after={}"\
           .format(subreddit, after)
    header = {"User-Agent": "MyApp/1.0"}

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        after = data.get("data").get("after")
        children_list = data.get("data").get("children")
        for items in children_list:
            parsed_list = items.get('data').get('title').lower().split()
            for element in parsed_list:
                if element in word_list:
                    if element in my_dict:
                        my_dict[element] += 1
                    else:
                        my_dict[element] = 1
        if after:
            count_words(subreddit, word_list, my_dict, after)

        # sort by values in descending order
            sorted_dict_desc = {k: v for k, v in sorted(my_dict.items(),
                                key=lambda item: item[1])}

            print(["{}: {}".format(k, v) for k, v in sorted_dict_desc.items()])
    else:
        return None
