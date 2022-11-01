#!/usr/bin/python3
"""
    A function that queries the Reddit API
"""
import json
import requests


def top_ten(subreddit):
    """
        Queries the top 10 hot posts
    """
    headers = {'User-Agent': 'MyAPI/v0.01'}
    parameters = {'limit': '10'}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=parameters)
    if response.status_code != 200:
        print(None)
        return
    dict_t = response.json()
    hot_posts = dict_t['data']['children']

    if len(hot_posts) == 0:
        print(None)
    else:
        for p in hot_posts:
            print(p['data']['title'])
