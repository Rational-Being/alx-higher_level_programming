#!/usr/bin/python3
"""
a python script that takes in a letter and send a POST request
to a URL sith the letter as a parameter
"""
from requests import post
from requests import codes
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) < 2:
        arg = {"q": ""}
    else:
        arg = {"q": argv[1]}
    response = post(url, data=arg)
    try:
        json = response.json()
        if len(obj) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(json['id'], json['name']))
    except Exception:
        print('Not a valid JSON')
