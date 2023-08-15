#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    new_list[idx] = element
    if 0 <= idx < len(new_list):
        return new_list
