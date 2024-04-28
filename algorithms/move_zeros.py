"""
    Develop an algorithm that rearranges an array by moving all zeros to the
    end while retaining the order of the remaining elements.

    Example:
    For the array
    [false, 1, 0, 1, 2, 0, 1, 3, "a"],
    the function move_zeros should return:
    [false, 1, 1, 2, 1, 3, "a", 0, 0].

    The time complexity of this algorithm is O(n).
"""
from typing import Any, List


# False == 0 is True
def move_zeros(seq: List[Any]):
    result = []
    zeros = 0

    for i in seq:

        if i == 0 and not isinstance(i, bool):

            zeros += 1

        else:
            result.append(i)

    result.extend([0] * zeros)

    return result


print(move_zeros([False, 1, 0, 1, 2, 0, [], 1, 3, "a"]))
