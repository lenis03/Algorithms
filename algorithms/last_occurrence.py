"""
    Find last occurance of a number in a sorted array (increasing order)
    Approach- Binary Search
    Time Complexity O(log n)
"""
from typing import List


def last_occurrence(array: List[int], target: int) -> int | None:
    """
    Returns the index of the last occurance of the given target in an array.
    The array has to be sorted in increasing order.
    """
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (high + low) // 2

        if (array[mid] == target and mid == len(array) - 1) or \
                (array[mid] == target and array[mid + 1] > target):
            return mid

        elif array[mid] <= target:
            low = mid + 1

        else:
            high = mid - 1


print(last_occurrence([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4], 3))
