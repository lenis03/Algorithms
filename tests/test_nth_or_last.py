import unittest

from algorithms.nth_or_last import nth_or_last


class NthOrLastTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(nth_or_last(range(3), 1), 1)
        self.assertEqual(nth_or_last(range(3), 3), 2)

    def test_default_value(self):
        default = 22
        self.assertEqual(nth_or_last(range(0), 5, default), default)

    def test_empty(self):
        self.assertRaises(ValueError, lambda: nth_or_last(range(0), 4))
