#!/usr/bin/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    totall = [total * weight for (total, weight) in my_list]
    w_total = [weight for (score, weight) in my_list]

    return sum(totall) / sum(w_total)
