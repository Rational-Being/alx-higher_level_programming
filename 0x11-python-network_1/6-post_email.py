#!/usr/bin/python3
"""
a python script that takes in a URL and an email addrress,
sends a POST request to the passed URL with the email as a parameter
and finally displays the body of the rreponse
"""
from requests import post
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email_value = {"email": argv[2]}
    response = post(url, data=email_value)
    print(response.text)
