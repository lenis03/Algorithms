"""
    This algorithm takes an array as input and returns
    the most frequently occurring value(s).
    In cases where there are multiple values that occur most frequently,
    the function returns a list containing all of them.
    This output can be utilized to identify a representative
    value within an array.

    The algorithm processes an input array by creating a dictionary
    to store the frequency of each element,
    determining the highest frequency count,
    and then compiling a list of the most frequent value(s).

    For example: Calling top_1([1, 1, 2, 2, 3, 4])
    will result in [1, 2] being returned.

    (TL:DR) Get mathematical Mode
    Complexity: O(n)
"""


def top_1(arry):
    values = {}
    # save each element of aary as key
    # save the number of repetitions each element as value
    result = []
    f_val = 0

    for val in arry:
        if val in values:
            values[val] += 1
        else:
            values[val] = 1

    f_val = max(values.values())

    for val in values.keys():
        if values[val] == f_val:
            result.append(val)
        else:
            continue

    return result
