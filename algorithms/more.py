from functools import partial
from itertools import islice, repeat
from collections.abc import Sequence
from collections import deque
from itertools import chain


_marker = object()


def take(iterable, n):
    return list(islice(iterable, n))


def raise_(exception, *args):
    raise exception(*args)


def chunked(iterable, n, strict=False):
    """Break *iterable* into lists of length *n*:

    >>> list(chunked([1, 2, 3, 4, 5, 6], 3))
    [[1, 2, 3], [4, 5, 6]]

    By the default, the last yielded list will have fewer than *n* elements
    if the length of *iterable* is not divisible by *n*:

        >>> list(chunked([1, 2, 3, 4, 5, 6, 7, 8], 3))
        [[1, 2, 3], [4, 5, 6], [7, 8]]

    If the length of *iterable* is not divisible by *n* and *strict* is
    ``True``, then ``ValueError`` will be raised before the last
    list is yielded.

    """
    iterator = iter(partial(take, iter(iterable), n), [])

    if strict:

        if n is None:
            raise ValueError('n cant be None when strict is True')

        def ret():
            for chunk in iterator:
                if len(chunk) != n:
                    raise ValueError('iterator cant divisible by n')
                yield chunk
        return iter(ret())

    return iterator


def first(iterable, default=_marker):
    """
    Return the first item of *iterable*, or *default* if *iterable* is
    empty.
        >>> first([0, 1, 2, 3])
        0
        >>> first([], 'some default')
        'some default'

    If *default* is not provided and there are no items in the iterable,
    raise ``ValueError``.

    :func:`first` is useful when you have a generator of expensive-to-retrieve
    values and want any arbitrary one. It is marginally shorter than
    ``next(iter(iterable), default)``.
    """
    try:
        return next(iter(iterable))

    except StopIteration as e:
        if default is _marker:
            raise ValueError('first() was called on an empty iterable object'
                             'and no default value was provided.') from e

        return default


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


def one(iterable, too_short=None, too_long=None):
    """
    Return the first item from *iterable*, which is expected to contain only
    that item. Raise an exception if *iterable* is empty or has more than one
    item.

    :func:`one` is useful for ensuring that an iterable contains only one item.
    For example, it can be used to retrieve the result of a database query
    that is expected to return a single row.

    If *iterable* is empty, ``ValueError`` will be raised. You may specify a
    different exception with the *too_short* keyword:

        >>> it = []
        >>> one(it)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        ValueError: too many items in iterable (expected 1)'
        >>> too_short = IndexError('too few items')
        >>> one(it, too_short=too_short)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        IndexError: too few items

    Similarly, if *iterable* contains more than one item, ``ValueError`` will
    be raised. You may specify a different exception with the *too_long*
    keyword:

        >>> it = ['too', 'many']
        >>> one(it)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        ValueError: Expected exactly one item in iterable, but got 'too',
        'many', and perhaps more.
        >>> too_long = RuntimeError
        >>> one(it, too_long=too_long)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        RuntimeError

    Note that :func:`one` attempts to advance *iterable* twice to ensure there
    is only one item. See :func:`spy` or :func:`peekable` to check iterable
    contents less destructively.

    """
    it = iter(iterable)

    try:
        first_value = next(it)

    except StopIteration as exc:
        raise (
            too_short or ValueError('too few items in iterable (expected 1)')
        ) from exc

    try:
        second_value = next(it)

    except StopIteration:
        pass

    else:
        msg = ('Expected exactly one item in iterable, but got {!r}, {!r}, '
               'and perhaps more.'.format(first_value, second_value)
               )
        raise too_long or ValueError(msg)

    return first_value


def interleave(*iterable):
    """
    Return a new iterable yielding from each iterable in turn,
    until the shortest is exhausted.

        >>> list(interleave([1, 2, 3], [4, 5], [6, 7, 8]))
        [1, 4, 6, 2, 5, 7]

    For a version that doesn't terminate after the shortest iterable is
    exhausted, see :func:`interleave_longest`.
    """
    return chain.from_iterable(zip(*iterable))


def repeat_each(iterable, n=2):
    """
    Repeat each element in *iterable* *n* times.

    >>> list(repeat_each('ABC', 3))
    ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C']
    """
    return chain.from_iterable(map(repeat, iterable, repeat(n)))


def strictly_n(iterable, n, too_short=None, too_long=None):
    """
    Validate that *iterable* has exactly *n* items and return them if
    it does. If it has fewer than *n* items, call function *too_short*
    with those items. If it has more than *n* items, call function
    *too_long* with the first ``n + 1`` items.

        >>> iterable = ['a', 'b', 'c', 'd']
        >>> n = 4
        >>> list(strictly_n(iterable, n))
        ['a', 'b', 'c', 'd']

    Note that the returned iterable must be consumed in order for the check to
    be made.

    By default, *too_short* and *too_long* are functions that raise
    ``ValueError``.

        >>> list(strictly_n('ab', 3))  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        ValueError: too few items in iterable (got 2)

        >>> list(strictly_n('abc', 2))  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        ValueError: too many items in iterable (got at least 3)

    You can instead supply functions that do something else.
    *too_short* will be called with the number of items in *iterable*.
    *too_long* will be called with `n + 1`.

        >>> def too_short(item_count):
        ...     raise RuntimeError
        >>> it = strictly_n('abcd', 6, too_short=too_short)
        >>> list(it)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        RuntimeError

        >>> def too_long(item_count):
        ...     print('The boss is going to hear about this')
        >>> it = strictly_n('abcdef', 4, too_long=too_long)
        >>> list(it)
        The boss is going to hear about this
        ['a', 'b', 'c', 'd']
    """

    # if we directly raise this error, we can't save this exception
    if too_short is None:
        too_short = lambda item_count: raise_(
            ValueError,
            f'too few items in iterable (got {item_count})'
        )

    if too_long is None:
        too_long = lambda item_count: raise_(
            ValueError,
            f'too many items in iterable (got at least {item_count})'
        )

    it = iter(iterable)

    for i in range(n):
        try:
            item = next(it)
        except StopIteration:
            too_short(i)
            return None
        yield item

    try:
        next(it)

    except StopIteration:
        pass

    else:
        too_long(n + 1)


def only(iterable, default=None, too_long=None):
    """
    If *iterable* has only one item, return it.
    If it has zero items, return *default*.
    If it has more than one item, raise the exception given by *too_long*,
    which is ``ValueError`` by default.

    >>> only([], default='missing')
    'missing'
    >>> only([1])
    1
    >>> only([1, 2])  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    ValueError: Expected exactly one item in iterable, but got 1, 2,
     and perhaps more.'
    >>> only([1, 2], too_long=TypeError)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    TypeError

    Note that :func:`only` attempts to advance *iterable* twice to ensure there
    is only one item.  See :func:`spy` or :func:`peekable` to check
    iterable contents less destructively.
    """

    it = iter(iterable)
    first_value = next(it, default)

    try:
        second_value = next(it)

    except StopIteration:
        pass

    else:
        msg = (
            'Expected exactly one item in iterable, '
            f'but got {first_value}, {second_value}, and perhaps more.'
        )
        raise too_long or ValueError(msg)

    return first_value


def always_reversible(iterable):
    """
    An extension of :func:`reversed` that supports all iterables, not
    just those which implement the ``Reversible`` or ``Sequence`` protocols.

        >>> print(*always_reversible(x for x in range(3)))
        2 1 0

    If the iterable is already reversible, this function returns the
    result of :func:`reversed()`. If the iterable is not reversible,
    this function will cache the remaining items in the iterable and
    yield them in reverse order, which may require significant storage.
    """

    try:
        return reversed(iterable)

    except TypeError:
        return reversed(list(iterable))


def always_iterable(obj, base_type=(str, bytes)):
    """
    If *obj* is iterable, return an iterator over its items::

        >>> obj = (1, 2, 3)
        >>> list(always_iterable(obj))
        [1, 2, 3]

    If *obj* is not iterable, return a one-item iterable containing *obj*::

        >>> obj = 1
        >>> list(always_iterable(obj))
        [1]

    If *obj* is ``None``, return an empty iterable:

        >>> obj = None
        >>> list(always_iterable(None))
        []

    By default, binary and text strings are not considered iterable::

        >>> obj = 'foo'
        >>> list(always_iterable(obj))
        ['foo']

    If *base_type* is set, objects for which ``isinstance(obj, base_type)``
    returns ``True`` won't be considered iterable.

        >>> obj = {'a': 1}
        >>> list(always_iterable(obj))  # Iterate over the dict's keys
        ['a']
        >>> list(always_iterable(obj, base_type=dict))  # Treat dicts as a unit
        [{'a': 1}]

    Set *base_type* to ``None`` to avoid any special handling and treat objects
    Python considers iterable as iterable:

        >>> obj = 'foo'
        >>> list(always_iterable(obj, base_type=None))
        ['f', 'o', 'o']
    """

    if obj is None:
        return iter(())

    if (base_type is not None) and isinstance(obj, base_type):
        return iter((obj, ))

    try:
        return iter(obj)

    except TypeError:
        return iter((obj, ))


def split_after(iterable, pred, max_split=-1):
    """
    Yield lists of items from *iterable*, where each list ends with an
    item where callable *pred* returns ``True``:

        >>> list(split_after('one1two2', lambda s: s.isdigit()))
        [['o', 'n', 'e', '1'], ['t', 'w', 'o', '2']]

        >>> list(split_after(range(10), lambda n: n % 3 == 0))
        [[0], [1, 2, 3], [4, 5, 6], [7, 8, 9]]

    At most *maxsplit* splits are done. If *maxsplit* is not specified or -1,
    then there is no limit on the number of splits:

        >>> list(split_after(range(10), lambda n: n % 3 == 0, maxsplit=2))
        [[0], [1, 2, 3], [4, 5, 6, 7, 8, 9]]
    """

    if max_split == 0:
        yield list(iterable)
        return

    buf = []
    it = iter(iterable)

    for item in it:
        buf.append(item)

        if pred(item) and buf:
            yield buf
            if max_split == 1:
                buf = list(it)
                if buf:
                    yield buf
                return

            buf = []
            max_split -= 1

    if buf:
        yield buf


def split_into(iterable, sizes):
    """
    Yield a list of sequential items from *iterable* of length 'n' for each
    integer 'n' in *sizes*.

        >>> list(split_into([1,2,3,4,5,6], [1,2,3]))
        [[1], [2, 3], [4, 5, 6]]

    If the sum of *sizes* is smaller than the length of *iterable*, then the
    remaining items of *iterable* will not be returned.

        >>> list(split_into([1,2,3,4,5,6], [2,3]))
        [[1, 2], [3, 4, 5]]

    If the sum of *sizes* is larger than the length of *iterable*, fewer items
    will be returned in the iteration that overruns *iterable* and further
    lists will be empty:

        >>> list(split_into([1,2,3,4], [1,2,3,4]))
        [[1], [2, 3], [4], []]

    When a ``None`` object is encountered in *sizes*, the returned list will
    contain items up to the end of *iterable* the same way that itertools.slice
    does:

        >>> list(split_into([1,2,3,4,5,6,7,8,9,0], [2,3,None]))
        [[1, 2], [3, 4, 5], [6, 7, 8, 9, 0]]

    :func:`split_into` can be useful for grouping a series of items where the
    sizes of the groups are not uniform. An example would be where in a row
    from a table, multiple columns represent elements of the same feature
    (e.g. a point represented by x,y,z) but, the format is not the same for
    all columns.
    """
    # convert the iterable argument into an iterator so its contents can
    # be consumed by islice in case it is a generator
    it = iter(iterable)
    for size in sizes:
        if size is None:
            yield list(it)
            return
        yield list(islice(it, size))
