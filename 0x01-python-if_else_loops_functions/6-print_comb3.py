#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
         comb3 = i * 10 + j
         if comb3 < 89:
            print("{:02d}".format(comb3), end=", ")
         else:
             print("89")
