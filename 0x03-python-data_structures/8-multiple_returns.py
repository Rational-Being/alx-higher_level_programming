#!/usr/bin/python3


def multiple_return(sentence):
    if len(sentence) == 0:
        frist_char = None
    else:
        frist_char = sentence[0]
    return (len(sentence), first_char)
