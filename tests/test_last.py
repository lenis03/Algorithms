import unittest

from algorithms.last_item import last


class LastTest(unittest.TestCase):
    def test_basic(self):
        cases = [
            (range(5), 4),
            (range(1), 0),
            (iter(range(5)), 4),
            (iter(range(1)), 0),
            ({i: str(i) for i in range(5)}, 4)
        ]
        for iterable, expected in cases:
            with self.subTest(iterable=iterable):
                self.assertEqual(last(iterable), expected)

    def test_default(self):
        cases = [
            (range(1), None, 0),
            ([], None, None),
            ({}, None, None),
            (iter([]), None, None)
        ]

        for iterable, default, excepted in cases:
            with self.subTest(iterable=iterable, default=default):
                self.assertEqual(last(iterable, default), excepted)

    def test_empty(self):
        for iterable in ([], iter(range(0))):
            with self.subTest(iterable=iterable):
                with self.assertRaises(ValueError):
                    last(iterable)
