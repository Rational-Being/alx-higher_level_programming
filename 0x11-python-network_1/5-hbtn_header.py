#!/usr/bin/bash
"""
this python script takes in a URl, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""

from requests import get
from sys import argv

if __name__ == __main__:
    response = get(argv[1]).headers.get(X-Request-Id)
    print(response)