"""
    Find the index of the given element in the array.
    There are no restrictions on the order of the elements in the array.
    If the element couldn't be found, returns None.
"""
from typing import List


def linear_search(array: List[int], target: int) -> int | None:
    for i in range(len(array)):
        if target == array[i]:
            return i

    return None
