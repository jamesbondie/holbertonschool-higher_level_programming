#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([2, 3, 5, 6, 6, 4]), 6)
        self.assertAlmostEqual(max_integer([-12, 0, 32, 97]), 97)
        self.assertAlmostEqual(max_integer([98, 1, 2, 3, 4]), 98)
        self.assertAlmostEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([98]), 98)
        self.assertAlmostEqual(max_integer([1, 2, 98, 4, 5]), 98)
