#!/usr/bin/python3
"""This script contains the number_of_subscribers function"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    for a given subreddit
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                    AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/117.0.0.0 Safari/537.36"
            }
    res = requests.get(url, headers=headers, allow_redirects=False)

    try:
        return res.json().get('data').get('subscribers')
    except Exception:
        return 0
