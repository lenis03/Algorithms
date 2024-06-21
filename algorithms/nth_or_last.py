from itertools import islice

from algorithms.last_item import last, _marker

# It's protected value and actually we shouldn't use and import it
# But we use it beacuse default value have a different memory address
# (if defined here) and value error doesn't work.
_marker = _marker


def nth_or_last(iterable, n, default=_marker):
    """
    Return the nth or the last item of *iterable*,
    or *default* if *iterable* is empty.

    >>> nth_or_last([0, 1, 2, 3], 2)
    2
    >>> nth_or_last([0, 1], 2)
    1
    >>> nth_or_last([], 0, 'some default')
    'some default'

    If *default* is not provided and there are no items in the iterable,
    raise ``ValueError``.
    """
    return last(islice(iterable, n + 1), default=default)
