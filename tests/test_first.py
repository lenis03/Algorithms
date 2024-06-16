import unittest
import traceback

from algorithms.first import first


class FirstTest(unittest.TestCase):

    def test_many_iterable_argument(self):
        self.assertEqual(first(i for i in range(90)), 0)

    def test_once_iterable_argument(self):
        self.assertEqual(first([3]), 3)

    def test_default_argument(self):
        self.assertEqual(first([], 22), 22)

    def test_empty_stop_iteration_raise(self):
        try:
            first([])
        except ValueError:
            formatted_exec = traceback.format_exc()
            self.assertIn(
                'StopIteration',
                formatted_exec
                )
            self.assertIn(
                'The above exception was the direct cause',
                formatted_exec
                )
        else:
            self.fail()
