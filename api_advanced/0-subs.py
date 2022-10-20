#!/usr/bin/python3
""""Doc"""
import requests


def number_of_subscribers(subreddit):
    """
    define the URL to fetch data from
    """

    base_url = "https://www.reddit.com/r/{}.json".format(subreddit)

    """
    initiate a response request using request.get
    """

    response = requests.get(base_url, headers={"user-agent": "Mozilla/5.0"})

    """
    convert the response gotten into a json
    """

    json_data = response.json()

    """
    Parse the Json to get the number of subscribers using .get()
    """

    if response.status_code == 200:
        return json_data.get("data").get("subscribers")
    else:
        return 0
