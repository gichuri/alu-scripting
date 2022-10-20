#!/usr/bin/python3
import requests
import json

def top_ten(subreddit):
    ''' 
    define the url and the query
    '''
    url = "https://www.reddit.com/r/{}/hot.json?limit=10&t=all".format(subreddit)

    '''
    make the request
    '''

    response = requests.get(url, headers = {'user-agent': 'youtbot'}).json()

    '''
    sieve through the JSON using a for loop
    '''
    try:
        posts = []

        for post in response['data']['children']:
            x = post['data']['title']
            posts.append(x)
        
        print(posts)
    except: 
        print(None) 
