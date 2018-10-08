import os
import sys

-
def get_cand(n, arr):
    cand = [1] * len(arr)

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            cand[i] = cand[i - 1] + 1
    for i in reversed(range(len(arr) - 1)):
        if arr[i] > arr[i + 1]:
            cand[i] = max(cand[i + 1] + 1, cand[i])

    return sum(cand)



n = 10
arr = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
cand = get_cand(n, arr)
print(str(cand))
