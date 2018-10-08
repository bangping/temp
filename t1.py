import os
import sys

def get_cand(n, arr):
    cur_m = arr[0]
    is_increase = None
    cur_num = 1
    prev_num = len(arr) + 1
    cand = 0
    for r in arr[1:]:
        if r != cur_m and is_increase is None:
            is_increase = (r > cur_m)
            cur_num += 1
            cur_m = r
        elif r != cur_m and is_increase == (r > cur_m):
            cur_num += 1
            cur_m = r
        else:
            cand += int((cur_num + 1) * cur_num / 2)
            if prev_num <= cur_num:
                cand += cur_num - prev_num + 1
            prev_num = cur_num
            cur_num = 1
            cur_m = r
            is_increase = None
    cand += int((cur_num + 1) * cur_num / 2)
    if prev_num <= cur_num:
        cand += cur_num - prev_num + 1
    return cand

n = 10
arr = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
cand = get_cand(n, arr)
print(str(cand))
