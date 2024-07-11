from time import sleep
import unittest
import traceback
from itertools import count, cycle


from algorithms.more import (
    take,
    chunked,
    first,
    last,
    nth_or_last,
    one,
    interleave,
    repeat_each,
    strictly_n,
    only,
    always_reversible,
    always_iterable,
    split_after,
    split_into,
    map_if,
    time_limited,

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


class InterleaveTest(unittest.TestCase):
    def test_even(self):
        actual = list((interleave([1, 4, 7], [2, 5, 8], [3, 6, 9])))
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(actual, expected)

    def test_short(self):
        actual = list((interleave([1, 4, 7], [2, 5, 8], [3, 6])))
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(actual, expected)

    def test_mixed_types(self):
        it_list = ['a', 'b', 'c', 'd']
        it_str = '123456'
        it_inf = count()
        actual = list(interleave(it_list, it_str, it_inf))
        expected = ['a', '1', 0, 'b', '2', 1, 'c', '3', 2, 'd', '4', 3]
        self.assertEqual(actual, expected)


class RepeatEachTest(unittest.TestCase):
    def test_default(self):
        actual = list(repeat_each('ABC'))
        expected = ['A', 'A', 'B', 'B', 'C', 'C']
        self.assertEqual(actual, expected)

    def test_basic(self):
        actual = list(repeat_each('ABC', 3))
        expected = ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C']
        self.assertEqual(actual, expected)

    def test_empty(self):
        actual = list(repeat_each([]))
        expected = []
        self.assertEqual(actual, expected)

    def test_no_repeat(self):
        actual = list(repeat_each('ABC', 0))
        expected = []
        self.assertEqual(actual, expected)

    def test_negative_repeat(self):
        actual = list(repeat_each('ABC', -1))
        expected = []
        self.assertEqual(actual, expected)

    def test_infinite_input(self):
        repeater = repeat_each(cycle('AB'))
        actual = take(repeater, 6)
        expected = ['A', 'A', 'B', 'B', 'A', 'A']
        self.assertEqual(actual, expected)


class StrictlyNTest(unittest.TestCase):

    def test_basic(self):
        iterable = ['a', 'b', 'c', 'd']
        n = 4
        actual = list(strictly_n(iterable, n))
        expected = iterable
        self.assertEqual(actual, expected)

    def test_too_short_default(self):
        iterable = ['a', 'b', 'c', 'd']
        n = 5

        with self.assertRaises(ValueError) as exc:
            list(strictly_n(iterable, n))

        self.assertEqual(
            'too few items in iterable (got 4)',
            exc.exception.args[0]
            )

    def test_too_long_default(self):
        iterable = ['a', 'b', 'c', 'd']
        n = 3

        with self.assertRaises(ValueError) as exc:
            list(strictly_n(iterable, n))

        self.assertEqual(
            'too many items in iterable (got at least 4)',
            exc.exception.args[0]
        )

    def test_too_short_custom(self):
        call_count = 0

        def too_short(item_count):
            nonlocal call_count
            call_count += 1

        iterable = ['a', 'b', 'c', 'd']
        n = 6
        actual = []

        for item in strictly_n(iterable, n, too_short=too_short):
            actual.append(item)

        expected = ['a', 'b', 'c', 'd']

        self.assertEqual(actual, expected)
        self.assertEqual(call_count, 1)

    def test_too_long_custom(self):
        import logging

        iterable = ['a', 'b', 'c', 'd']
        n = 2

        too_long = lambda item_count: logging.warning(
            'Picked the first %s items', n
        )

        with self.assertLogs(level='WARNING') as exc:
            actual = list(strictly_n(iterable, n, too_long=too_long))

        self.assertEqual(actual, ['a', 'b'])
        self.assertIn('Picked the first 2 items', exc.output[0])


class OnlyTest(unittest.TestCase):
    def test_defaults(self):
        self.assertEqual(only([]), None)
        self.assertEqual(only([1]), 1)
        self.assertRaises(ValueError, lambda: only([1, 2, 4]))
        # Why we use lambda? because if we don't use it raises error stops our
        # program, then we use lamda to returen raises error!

    def test_custom_default_value(self):
        self.assertEqual(only([], default='!'), '!')
        self.assertEqual(only([2], default=44), 2)
        self.assertRaises(
            ValueError,
            lambda: only([22, 44, 11], default='some default')
            )

    def test_custom_exception(self):
        self.assertEqual(only([], too_long=RuntimeError), None)
        self.assertEqual(only([1], too_long=RuntimeError), 1)
        self.assertRaises(
            RuntimeError,
            lambda: only([11, 22], too_long=RuntimeError)
            )

    def test_default_exception_message(self):
        self.assertRaisesRegex(
            ValueError,
            'Expected exactly one item in iterable, '
            'but got foo, bar, and perhaps more.',
            lambda: only(['foo', 'bar', 'baz'])
        )


class AlwaysReversibleTest(unittest.TestCase):

    def test_regular_reversed(self):

        self.assertEqual(
            list(reversed(range(10))),
            list(always_reversible(range(10)))
        )
        self.assertEqual(
            list(reversed([1, 2, 3, 4])),
            list(always_reversible([1, 2, 3, 4]))
            )
        self.assertEqual(
            reversed([1, 2, 3, 4]).__class__,
            always_reversible([1, 2, 3, 4]).__class__)

    def test_nonseq_reversed(self):

        self.assertEqual(
            list(reversed(range(10))),
            list(always_reversible(i for i in range(10)))
        )
        self.assertEqual(
            list(reversed([1, 2, 3])),
            list(always_reversible(i for i in [1, 2, 3]))
        )
        self.assertNotEqual(
            reversed((1, 2)).__class__,
            always_reversible(i for i in (1, 2)).__class__
            )


class AlwaysIterableTest(unittest.TestCase):
    def test_single(self):
        self.assertEqual(list(always_iterable(1)), [1])

    def test_string(self):
        for obj in ['foo', b'bar', 'baz']:
            actual = list(always_iterable(obj))
            excpected = [obj]
            self.assertEqual(actual, excpected)

    def test_base_type(self):
        dict_obj = {'a': 1, 'b': 2}
        str_obj = '123'

        # Default: dicts are iterable like they normally are
        default_actual = list(always_iterable(dict_obj))
        default_expected = list(dict_obj)
        self.assertEqual(default_actual, default_expected)

        # Unitary types set: dicts are not iterable
        custom_actual = list(always_iterable(dict_obj, base_type=dict))
        custom_expected = [dict_obj]
        self.assertEqual(custom_actual, custom_expected)

        # With unitary types set, strings are iterable
        str_actual = list(always_iterable(str_obj, base_type=None))
        str_excepted = list(str_obj)
        self.assertEqual(str_actual, str_excepted)

        # base_type handles nested tuple (via isinstance).
        base_type = ((dict,),)
        custom_actual = list(always_iterable(dict_obj, base_type=base_type))
        custom_expected = [dict_obj]
        self.assertEqual(custom_actual, custom_expected)

    def test_iterable(self):
        self.assertEqual(
            list(always_iterable([0, 1])),
            [0, 1])
        self.assertEqual(
            list(always_iterable([0, 1], base_type=list)),
            [[0, 1]])
        self.assertEqual(
            list(always_iterable(iter('foo'))),
            ['f', 'o', 'o'])
        self.assertEqual(
            list(always_iterable([])),
            [])

    def test_none(self):
        self.assertEqual(list(always_iterable(None)), [])

    def test_generator(self):
        def _gen():
            yield 0
            yield 1
        self.assertEqual(list(always_iterable(_gen())), [0, 1])


class SplitAfterTest(unittest.TestCase):
    def test_start_with_sep(self):
        actual = list(split_after('xooxoo', lambda c: c == 'x'))
        expected = [['x'], ['o', 'o', 'x'], ['o', 'o']]
        self.assertEqual(actual, expected)

    def test_ends_with_sep(self):
        actual = list(split_after('ooxoox', lambda c: c == 'x'))
        expected = [['o', 'o', 'x'], ['o', 'o', 'x']]
        self.assertEqual(actual, expected)

    def test_no_sep(self):
        actual = list(split_after('ooo', lambda c: c == 'x'))
        expected = [['o', 'o', 'o']]
        self.assertEqual(actual, expected)

    def test_max_split(self):
        for args, expected in [
            (
                ('a,b,c,d', lambda c: c == ',', -1),
                [['a', ','], ['b', ','], ['c', ','], ['d']]
            ),
            (
                ('a,b,c,d', lambda c: c == ',', 0),
                [['a', ',', 'b', ',', 'c', ',', 'd']]
            ),
            (
                ('a,b,c,d', lambda c: c == ',', 1),
                [['a', ','], ['b', ',', 'c', ',', 'd']]
            ),
            (
                ('a,b,c,d', lambda c: c == ',', 2),
                [['a', ','], ['b', ','], ['c', ',', 'd']]
            ),
            (
                ('a,b,c,d', lambda c: c == ',', 10),
                [['a', ','], ['b', ','], ['c', ','], ['d']]
            ),
            (
                ('a,b,c,d', lambda c: c == '@', 2),
                [['a', ',', 'b', ',', 'c', ',', 'd']]
            )
        ]:
            actual = list(split_after(*args))
            self.assertEqual(actual, expected)


class SplitIntoTest(unittest.TestCase):
    def test_iterable_just_right(self):
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sizes = [2, 3, 4]
        actual = list(split_into(iterable, sizes))
        expected = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
        self.assertEqual(actual, expected)

    def test_iterable_too_small(self):
        iterable = [1, 2, 3, 4, 5, 6]
        sizes = [2, 3, 4]
        actual = list(split_into(iterable, sizes))
        expected = [[1, 2], [3, 4, 5], [6]]
        self.assertEqual(actual, expected)

    def test_iterbale_too_small_extra(self):
        iterable = [1, 2, 3, 4, 5, 6]
        sizes = [2, 3, 4, 5]
        actual = list(split_into(iterable, sizes))
        expected = [[1, 2], [3, 4, 5], [6], []]
        self.assertEqual(actual, expected)

    def test_iterable_too_large(self):
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sizes = [2, 3, 2]
        actual = list(split_into(iterable, sizes))
        expected = [[1, 2], [3, 4, 5], [6, 7]]
        self.assertEqual(actual, expected)

    def test_using_none_with_leftover(self):
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sizes = [2, 3, None]
        actual = list(split_into(iterable, sizes))
        expected = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
        self.assertEqual(actual, expected)

    def test_using_none_without_leftover(self):
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sizes = [2, 3, 4, None]
        actual = list(split_into(iterable, sizes))
        expected = [[1, 2], [3, 4, 5], [6, 7, 8, 9], []]
        self.assertEqual(actual, expected)

    def test_using_none_mid_size(self):
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sizes = [2, 3, None, 4]
        actual = list(split_into(iterable, sizes))
        expected = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
        self.assertEqual(actual, expected)

    def test_iterable_empty(self):
        iterable = []
        sizes = [2, 3, 2]
        actual = list(split_into(iterable, sizes))
        expected = [[], [], []]
        self.assertEqual(actual, expected)

    def test_iterable_empty_using_none(self):
        iterable = []
        sizes = [2, 3, None, 2]
        actual = list(split_into(iterable, sizes))
        expected = [[], [], []]
        self.assertEqual(actual, expected)

    def test_sizes_empty(self):
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sizes = []
        actual = list(split_into(iterable, sizes))
        expected = []
        self.assertEqual(actual, expected)

    def test_both_empty(self):
        iterable = []
        sizes = []
        actual = list(split_into(iterable, sizes))
        expected = []
        self.assertEqual(actual, expected)

    def test_bool_in_sizes(self):
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sizes = [False, 3, True, 4]
        actual = list(split_into(iterable, sizes))
        expected = [[], [1, 2, 3], [4], [5, 6, 7, 8]]
        self.assertEqual(actual, expected)

    def test_invalid_in_sizes(self):
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sizes = [3, [], 2]
        with self.assertRaises(ValueError):
            list(split_into(iterable, sizes))

    def test_invalid_in_sizes_after_none(self):
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sizes = [2, 3, None, []]
        actual = list(split_into(iterable, sizes))
        expected = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
        self.assertEqual(actual, expected)

    def test_generator_iterable_integrity(self):
        iterable = (i for i in range(10))
        sizes = [2, 3]
        actual = list(split_into(iterable, sizes))
        expected = [[0, 1], [2, 3, 4]]
        self.assertEqual(actual, expected)

        iterable_actual = list(iterable)
        iterable_expected = [5, 6, 7, 8, 9]
        self.assertEqual(iterable_actual, iterable_expected)

    def test_generator_sizes_integrity(self):
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sizes = (i for i in [2, 3, None, 5, 7])
        actual = list(split_into(iterable, sizes))
        expected = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
        self.assertEqual(actual, expected)

        sizes_actual = list(sizes)
        sizes_expected = [5, 7]
        self.assertEqual(sizes_expected, sizes_actual)


class MapIfTest(unittest.TestCase):
    def test_without_func_else(self):
        iterable = list(range(-5, 5))
        actual = list(map_if(iterable, lambda x: x > 3, lambda x: 'toobig'))
        expected = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 'toobig']
        self.assertEqual(actual, expected)

    def test_with_func_else(self):
        iterable = list(range(-5, 5))
        actual = list(map_if(
            iterable,
            lambda x: x >= 0,
            lambda x: 'notneg',
            lambda x: 'neg'
            ))
        expected = ['neg'] * 5 + ['notneg'] * 5
        self.assertEqual(actual, expected)

    def test_empty(self):
        actual = list(map_if([], lambda x: x > 5, lambda x: None))
        expected = []
        self.assertEqual(actual, expected)


class TimeLimitedTest(unittest.TestCase):
    def test_basic(self):
        def _generator():
            yield 1
            yield 2
            sleep(0.2)
            yield 3

        iterable = time_limited(0.1, _generator())
        actual = list(iterable)
        expected = [1, 2]
        self.assertEqual(actual, expected)
        self.assertTrue(iterable.timed_out)

    def test_complete(self):
        iterable = time_limited(2, range(10))
        actual = list(iterable)
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(actual, expected)
        self.assertFalse(iterable.timed_out)

    def test_zero_limit(self):
        iterable = time_limited(0, count())
        actual = list(iterable)
        expected = []
        self.assertEqual(actual, expected)
        self.assertTrue(iterable.timed_out)

    def test_invalid_limit(self):
        with self.assertRaises(ValueError):
            list(time_limited(-0.1, count()))


if __name__ == '__main__':
    unittest.main()
