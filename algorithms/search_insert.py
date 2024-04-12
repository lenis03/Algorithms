"""
   Given a sorted array and a target value, the task is to find the
   index where the target value should be placed in the array to
   maintain its sorted order. If the target value is already in the array,
   return its index. Otherwise, return the index where the target value would
   be inserted to keep the array sorted.

    For example:
    - In the array [1, 3, 5, 6] with the target value 5,
    the expected result is index 2.
    - For [1, 3, 5, 6] with the target value 2, the expected index is 1.
    - If the array is [1, 3, 5, 6] and the target value is 7, the index to be
    returned is 4.
    - When dealing with the array [1, 3, 5, 6] and the target value 0,
    the index to be returned should be 0.

    This algorithm aims to efficiently determine the appropriate index for
    inserting the target value into the sorted array or identifying the
    correct index if the value is already present.
"""
from typing import List


def search_insert(arry: List[int], val: int) -> int:
    low = 0
    hight = len(arry) - 1
    mid = hight // 2

    while low <= hight:
        if val > arry[mid]:
            mid += 1
            low = mid
        else:
            mid -= 1
            hight = mid
    return low
