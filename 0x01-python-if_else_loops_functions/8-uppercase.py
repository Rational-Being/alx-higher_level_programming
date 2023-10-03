#!/usr/bin/python3


def uppercase(str):
    for var in str:
        var = ord(c)
        if var >= 97 and var <= 122:
            var = var - 32
        print(f"{var}", end="")
        #print("{:c}".format(var), end="")
    print()
