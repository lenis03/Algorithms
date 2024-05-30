"""
    If we have an array of integers sorted in ascending order, we need to find
    the starting and ending position of a given target value.
    If the target is not found in the array, we should
    return [None, None].

    For example:
    Input: nums = [5,7,7,8,8,8,10], target = 8
    Output: [3,5]
    Input: nums = [5,7,7,8,8,8,10], target = 11
    Output: [None, None]
"""
from typing import List


def search_range(arry: List[int], target: int):
    low = 0
    high = len(arry) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if target < arry[mid]:
            high = mid - 1

        elif target > arry[mid]:
            low = mid + 1

        else:
            break

    for i in range(len(arry) - 1, -1, -1):
        if arry[i] == target:
            return [mid, i]

    return [None, None]
