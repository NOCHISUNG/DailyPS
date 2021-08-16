#pypy3

import sys

input = sys.stdin.readline


def update(idx):
    idx += size
    tree[idx] = 1
    while idx > 1:
        idx >>= 1
        tree[idx] += 1


def total(left, right):
    left += size
    right += size
    ret = 0

    while left <= right:
        if left % 2 == 1:
            ret += tree[left]
            left += 1
        if right % 2 == 0:
            ret += tree[right]
            right -= 1
        left >>= 1
        right >>= 1

    return ret


n = int(input())
A = input().split()
B = input().split()

adB = dict()
for i, a in enumerate(A):
    adB[a] = i

h = n.bit_length()
size = 1 << h
tree = [0] * (2 * size)

ans = 0
for b in B:
    idx = adB[b]
    ans += total(idx, n)
    update(idx)

print(ans)
