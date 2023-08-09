#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 100 + 1):
        number = i
        if i % 3 == 0:
            number = "Fizz"
        if i % 5 == 0:
            number = "Buzz"
        if i % 3 == 0 and i % 5 == 0:
            number = "FizzBuzz"
        print(number, end=' ')
