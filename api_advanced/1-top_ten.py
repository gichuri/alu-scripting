#!/usr/bin/python3
"""
python script to fetch the titles of hottest 10 posts on a subreddit

"""


import requests


def top_ten(subreddit):
    """
    define the url and the query
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    """
    make the request
    """

    response = requests.get(url, headers={"user-agent": "youtbot"})

    """
    sieve through the JSON using a for loop
    """
    if response.status_code == 200:
        json_data = response.json

        for i in range(10):
            print(json_data.get("data").get("children").get("data").get("title"))
    else:
        print(None)
