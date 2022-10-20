#!/usr/bin/python3
"""
python script to fetch the titles of hottest 10 posts on a subreddit

"""


import requests


def top_ten(subreddit):
    """
    define the url and the query
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=8".format(subreddit)

    """
    make the request
    """

    response = requests.get(url, headers={"user-agent": "youtbot"}).json()

    """
    sieve through the JSON using a for loop
    """
    try:
        posts = []

        for post in response["data"]["children"]:
            x = post["data"]["title"]
            posts.append(x)
        for element in posts:
            print(element)
    except:
        print(None)

