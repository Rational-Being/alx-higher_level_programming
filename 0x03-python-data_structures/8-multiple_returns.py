#!/usr/bin/python3


def multiple_return(sentence):
    if sentence != "":
        frist_char = sentence[0]
    else:
        frist_char = None
    return (len(sentence), first_char)
