#!/usr/bin/python3

"""
this script fetches the url provided in the code using the request package
the package requests must be use
the body of the request should display in tabular form
"""

from requests import get

if __name__ == "__main__":
    response = get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
