#!/usr/bin/python3
"""
this script fetches the url provided in the code
using the request package
"""
from requests import get
if __name__ == "__main__":
    response = get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
