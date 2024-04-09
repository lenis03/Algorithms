"""
    At times, it's necessary to filter arrays based on specific criteria
    such as selecting values greater than 10 or less than 100.
    Utilizing this algorithm allows you to confine your
    array to a particular range.

    Given an array and minimum and maximum values,
    this function returns an array comprising values from the original array
    that are greater than the minimum value and less than the maximum value.
    If you intend to only apply a lower or upper limit,
    you should input 'unlimit'.

    Example: `limit([1,2,3,4,5], None, 3) = [1,2,3]`

    Algorithm Complexity = O(n)
"""


def limit(arry, min_lim=None, max_lim=None):
    min_check = lambda val: True if min_lim is None else (val >= min_lim)
    max_check = lambda val: True if max_lim is None else (val <= max_lim)

    return [val for val in arry if min_check(val) and max_check(val)]


def limit2(arry, min_lim=None, max_lim=None):
    if len(arry) == 0:
        return arry

    if min_lim is None:
        min_lim = min(arry)

    if max_lim is None:
        max_lim = max(arry)

    return list(filter(lambda val: min_lim <= val <= max_lim, arry))
