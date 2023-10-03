#!/usr/bin/python3
for f_digit in range(0, 10):
    for s_digit in range(f_digit, 10):
        if f_digit == s_digit:
            continue
        else:
            if f_digit == 8 and s_digit == 9:
                print("{}{} ".format(f_digit, s_digit), end="")
            else:
                print("{}{}, ".format(f_digit, s_digit), end="")
