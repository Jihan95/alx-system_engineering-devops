#!/usr/bin/python3
"""Top Ten"""
import requests


def top_ten(subreddit):
    """ function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'MyRedditApp/1.0'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print('None')
