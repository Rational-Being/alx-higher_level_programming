#!/usr/bin/python3

"""
a pythn script that takes ina URL, senda request to the URL
and displays the value found un the header of the resppkonse
"""
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        print(response.info()['X-Request-Id'])
