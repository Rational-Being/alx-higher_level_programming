#!/usr/bin/python3
import sys

if __name__ == "__main__":
    i = len(sys.argv) - 1

    if i == 0:
        print("0 arguments")
    elif i == 1:
        print("1 argument:")
        print("1: {:s}".format(sys.argv[1]))
    elif i > 1:
        print("{:d} arguments:".format(i))
        for count in range(1, i + 1):
            print("{:d}: {:s}".format(count, sys.argv[count]))
