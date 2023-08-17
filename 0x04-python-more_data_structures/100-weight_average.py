#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    nbr = 0
    d_nbr = 0

    for i in my_list:
        nbr += i[0] * i[1]
        d_nbr += i[1]

    return (nbr / d_nbr)
