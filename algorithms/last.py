from collections.abc import Sequence
from collections import deque


_marker = object()


def last(iterable, default=_marker):
    """
    Return the last item of *iterable*, or *default* if *iterable* is
    empty.

        >>> last([0, 1, 2, 3])
        3
        >>> last([], 'some default')
        'some default'

    If *default* is not provided and there are no items in the iterable,
    raise ``ValueError``.
    """

    try:
        if isinstance(iterable, Sequence):
            return iterable[-1]

        elif hasattr(iterable, '__reversed__'):
            return next(reversed(iterable))

        else:
            return deque(iterable, maxlen=1)[-1]

    except (IndexError, TypeError, StopIteration):
        if default is _marker:
            raise ValueError('last() called on an empty iterable object,'
                             'and no default value was provided.'
                             )
        return default
