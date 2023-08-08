#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        comb = (i * 10) + j
        if comb < 89:
            print("{:02d}".format(comb), end=", ")
        else:
            print("89")
