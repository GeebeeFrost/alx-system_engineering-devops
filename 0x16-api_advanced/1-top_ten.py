#!/usr/bin/python3
"""This script contains the top_ten function"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10
    hot posts for a given subreddit
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                    AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/117.0.0.0 Safari/537.36"
            }
    params = {'limit': 10}
    res = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )

    try:
        posts = res.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    except Exception:
        print(None)
