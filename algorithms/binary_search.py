"""
    Binary Search

    Find an element in a sorted array (in ascending order).
    [2, 4, 8, 10, 22, 33, 44, 99, 102, 105] 99 ==> 7

    Time Complexity O(log(n))
"""
from typing import List


def binary_search(array: List[int], target: int) -> int | None:
    low, high = 0, len(array) - 1

    while low < high:
        mid = (high + low) // 2
        val = array[mid]

        if val == target:
            return mid

        elif val < target:
            low = mid + 1

        else:
            high = mid - 1

    return None


print(binary_search([2, 4, 8, 10, 22, 33, 44, 99, 102, 105], 99))
