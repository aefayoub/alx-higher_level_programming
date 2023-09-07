#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Max integer - Unittest
    """

    def max_integer(self):
        self.assertEqual(max_integer([5, -2, 100, 3]), 100)

    def empty_list(self):
        self.assertEqual(max_integer([]), None)

    def repeated_number(self):
        self.assertEqual(max_integer([1000, 1000, 1000]), 1000)

    def float_numbers(self):
        self.assertEqual(max_integer([50, 51, 50, 49]), 51)

    def max_operated_integer(self):
        self.assertEqual(max_integer([-3, -5 * -5, 12, -1]), 25)

    def neg_numbers(self):
        self.assertEqual(max_integer([-10, -5, -2, -1]), -1)

    def max_at_beginning(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def zero_number(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def big_list(self):
        self.assertEqual(max_integer([
            901, 902, 903, 904, 905, 906, 907, 908, 909, 910,
            911, 912, 913, 914, 915, 916, 917, 918, 919, 920,
            919, 918, 917, 1000, 915, 914, 913, 912, 911, 910,
            909, 908, 907, 906, 905, 904, 903, 902, 901]), 1000)

    def list_with_loop(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

    def one_number_in_a_list(self):
        self.assertEqual(max_integer([1]), 1)

    def string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

    def dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    def number(self):
        with self.assertRaises(TypeError):
            max_integer(1)
