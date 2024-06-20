#!/usr/bin/python3
""" How many subs? """
import requests


def number_of_subscribers(subreddit):
    """ function that returns numbers of subs """
    url = f"https://oauth.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'MyRedditApp/1.0'
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
