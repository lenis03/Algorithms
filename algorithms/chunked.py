from functools import partial
from itertools import islice


def take(iterable, n):
    return list(islice(iterable, n))


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
