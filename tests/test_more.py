import unittest
import traceback
from itertools import count


from algorithms.more import (
    take,
    chunked,
    first,
    last,
    nth_or_last,
    one

)


class TakeTest(unittest.TestCase):

    def test_simple_take(self):
        t = take(range(10), 5)
        self.assertEqual(t, [0, 1, 2, 3, 4])

    def test_null_second_argument_take(self):
        t = take(range(10), 0)
        self.assertEqual(t, [])

    def test_negative_first_argument_take(self):
        self.assertRaises(TypeError, lambda: take(-10, 5))

    def test_too_much_n_take(self):
        t = take(range(5), 10)
        self.assertEqual(t, [0, 1, 2, 3, 4])

    def test_negative_second_argument_take(self):
        self.assertRaises(ValueError, lambda: take(range(5), -3))


class ChunkedTest(unittest.TestCase):

    def test_even_iterable_value_chunked(self):

        self.assertEqual(
            list(chunked('ABCDEF', 3)),
            [['A', 'B', 'C'], ['D', 'E', 'F']]
            )

    def test_odd_iterable_value_chunked(self):

        self.assertEqual(
            list(chunked('ABCDE', 3)),
            [['A', 'B', 'C'], ['D', 'E']]
        )

    def test_none_n_value_chunked(self):

        self.assertEqual(
            list(chunked('ABCDEF', None)),
            [['A', 'B', 'C', 'D', 'E', 'F']]
        )

    def test_false_strict_chunked(self):
        self.assertEqual(
            list(chunked('ABCDEF', 3, strict=False)),
            [['A', 'B', 'C'], ['D', 'E', 'F']]
            )

    def test_true_strict_chunked(self):
        def f():
            return list(chunked('ABCDE', 3, strict=True))

        self.assertRaisesRegex(ValueError, 'iterator cant divisible by n', f)
        self.assertEqual(
            list(chunked('ABCDEF', 3, strict=True)),
            [['A', 'B', 'C'], ['D', 'E', 'F']]
        )

    def test_true_strict_with_none_n_value_chunked(self):
        def f():
            return list(chunked('ABCDE', None, strict=True))

        self.assertRaisesRegex(
            ValueError,
            'n cant be None when strict is True',
            f
            )


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


class NthOrLastTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(nth_or_last(range(3), 1), 1)
        self.assertEqual(nth_or_last(range(3), 3), 2)

    def test_default_value(self):
        default = 22
        self.assertEqual(nth_or_last(range(0), 5, default), default)

    def test_empty(self):
        self.assertRaises(ValueError, lambda: nth_or_last(range(0), 4))


class OneTest(unittest.TestCase):

    def test_basic(self):
        it = ['item']
        self.assertEqual(one(it), 'item')

    def test_too_short(self):
        it = []
        for too_short, exc_type in [
            (None, ValueError),
            (StopIteration, StopIteration)
        ]:
            with self.subTest(too_short=too_short):
                try:
                    one(it, too_short)
                except exc_type:
                    formatted_exc = traceback.format_exc()
                    self.assertIn(
                        'StopIteration',
                        formatted_exc
                        )
                    self.assertIn(
                        'The above exception was the direct cause',
                        formatted_exc
                        )

    def test_too_long(self):
        it = count()
        self.assertRaises(ValueError, lambda: one(it))
        self.assertEqual(next(it), 2)
        self.assertRaises(
            OverflowError,
            lambda: one(it, too_long=OverflowError)
            )

    def test_too_long_default_message(self):
        it = count()

        self.assertRaisesRegex(
            ValueError,
            'Expected exactly one item in iterable, but got 0, 1, '
            'and perhaps more.',
            lambda: one(it)
        )


if __name__ == '__main__':
    unittest.main()
