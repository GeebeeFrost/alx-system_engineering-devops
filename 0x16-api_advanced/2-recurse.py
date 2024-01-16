#!/usr/bin/python3
"""This script contains the recurse function"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursively queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
    """
    if not subreddit or not isinstance(subreddit, str):
        return None
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                    AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/117.0.0.0 Safari/537.36"
                    }
    params = {'after': after}  # parameter to contain anchor item
    res = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )
    if res.status_code == 200:
        anchor_item = res.json().get('data').get('after')
        if anchor_item:
            after = anchor_item
            recurse(subreddit, hot_list, after)
        posts = res.json().get('data').get('children')
        for post in posts:
            hot_list.append(post.get('data').get('title'))
        return hot_list
    else:
        return None
