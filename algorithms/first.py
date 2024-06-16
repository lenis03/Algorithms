_marker = object()


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
