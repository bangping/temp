
import os
import sys

def max_sum(arr):
    if len(arr) < 3:
        return 0

    sum_end = [0] * len(arr)
    sum_end[0] = arr[0]
    sum_end[1] = arr[1]

    ms = -sys.maxint-1
    for i in range(2, len(arr)):
        cs = sum_end[i - 2] + arr[i]
        ms = max(ms, cs)
        sum_end[i] = max(ms, arr[i])

    return ms

arr = [-2, 1, 3, -4, 5]
ms = max_sum(arr)
print(ms)
