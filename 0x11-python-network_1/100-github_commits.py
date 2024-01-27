#!/usr/bin/python3
"""
a python script that takes two argument
and list 10 commits form the most recent to tolder of the repository
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = get(url)
    j = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(j[i].get("sha"),
                j[i].get("commit").get("author")
                .get("name")))
    except ValueError:
        pass
