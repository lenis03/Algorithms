import unittest

from algorithms.chunked import take, chunked


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


if __name__ == '__main__':
    unittest.main()
