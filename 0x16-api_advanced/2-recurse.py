#!/usr/bin/python3
"""
    A recursivve fuction that queries the Reddit API
    and returns the tiles of all hot articles
"""


import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
        Quries the Reddit API
    """
    global after
    headers = {'User-Agent': 'MyAPI/v0.01'}
    parameters = {'after': after}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=parameters)
    if response.status_code != 200:
        print(None)
        return None
    nxt = response.json().get('data').get('after')
    if nxt is not None:
        after = nxt
        recurse(subreddit, hot_list)
    titles = response.json().get('data').get('children')
    for title in titles:
        hot_list.append(title.get('data').get('title'))
    return hot_list
