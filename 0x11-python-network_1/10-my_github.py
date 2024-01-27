#!/usr/bin/python3
"""
a python script that takes in a letter and send a POST request
to a URL sith the letter as a parameter
"""
from requests import get
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = "https://api.github.com/user"
    response = get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(response.json().get("id"))
