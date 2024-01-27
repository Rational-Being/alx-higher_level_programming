#!/usr/bin/python3
"""
this python script takes in a URl, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = get(url).headers.get('x-Request-id')
    print(response)
