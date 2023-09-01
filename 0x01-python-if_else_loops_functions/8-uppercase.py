#!/usr/bin/python3

def uppercase(str):
    for char in str:
        upperchar = chr(ord(char) - ord('a') + ord('A'))
        print("{}".format(upperchar) if 'a' <= char <= 'z' else char, end='')
    print()
