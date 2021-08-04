import sys
from math import log, ceil
input = sys.stdin.readline


def modify(idx, val):
    idx += size - 1
    arr[idx] = val
    while idx > 1:
        idx //= 2
        arr[idx] = arr[idx*2] + arr[idx*2 + 1]


def total(root, left, right, start, end):
    if right < start or end < left:
        return 0
    if start <= left and right <= end:
        return arr[root]

    mid = (left + right)//2
    return total(root*2, left, mid, start, end) + total(root*2+1, mid+1, right, start, end)
    

n, m = map(int, input().split())
size = 2 ** ceil(log(n, 2))
arr = [0 for x in range(2 * size)]

for _ in range(m):
    cmd, i, j = map(int, input().split())

    #sum
    if cmd == 0:
        if i > j:
            i, j = j, i
        print(total(1, 0, size-1, i-1, j-1))
    #modify
    elif cmd == 1:
        modify(i, j)
        
