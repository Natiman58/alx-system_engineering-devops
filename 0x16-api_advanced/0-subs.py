#!/usr/bin/python3
"""
    A function that queries the Reddit API
    and returns the nuber of subscribers for a given subreddit
"""


import requests
import json

def number_of_subscribers(subreddit):
    """ Queries to Reddit API
        and returns the no of subscribers to a given subreddit
    """

    headers = {'User-Agent': 'MyAPI/v0.01'}

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    dict_t = response.json()
    if 'data' not in dict_t:
        return 0
    if 'subscribers' not in dict_t.get('data'):
        return 0
    return response.json()['data']['subscribers']
