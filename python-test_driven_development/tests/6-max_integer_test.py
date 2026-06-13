#!/usr/bin/python3
"""Unittest for max_integer"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_max(self):
        self.assertEqual(max_integer([1, 1, 1, 5, 1]), 5)

    def test_float_list(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_string(self):
        self.assertEqual(max_integer("Bach"), "h")


if __name__ == "__main__":
    unittest.main()
