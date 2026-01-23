#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    # --- Cas de base ---
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_default_empty(self):
        self.assertIsNone(max_integer())

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    # --- Max position ---
    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 10, 3, 4]), 10)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 99]), 99)

    # --- Nombres négatifs ---
    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -3, -9, -2]), -1)

    def test_negative_and_positive(self):
        self.assertEqual(max_integer([-10, 0, 5, -2]), 5)

    # --- Doublons ---
    def test_duplicates(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_duplicates_with_max(self):
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)

    # --- Floats ---
    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 2.6]), 2.7)

    def test_int_and_float(self):
        self.assertEqual(max_integer([1, 2.0, 3, 2.9]), 3)

    # --- Strings (Python compare lexicographique) ---
    def test_strings(self):
        self.assertEqual(max_integer(["a", "z", "b"]), "z")

    # --- Cas plus “gros” ---
    def test_long_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 100, 6, 7]), 100)


if __name__ == "__main__":
    unittest.main()