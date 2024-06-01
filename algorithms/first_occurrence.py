"""
    Find first occurance of a number in a sorted array (increasing order)
    Approach- Binary Search
    Time Complexity O(log n)
"""
from typing import List


def first_occurrence(array: List[int], target: int) -> int | None:
    """
    Returns the index of the first occurance of the given target in an array.
    The array has to be sorted in increasing order.
    """
    low, high = 0, len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2  # for get mid in integer range

        if low == high:
            break

        if array[mid] < target:
            low = mid + 1

        else:
            high = mid

    if array[low] == target:
        return low


print(first_occurrence([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4], 4))
