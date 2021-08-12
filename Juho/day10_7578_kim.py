"""
input :
5
132 392 311 351 231
392 351 132 311 231

output :
3
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
PIV = 1 << 19
TREE = [0 for _ in range(2 * PIV)]


def update(ind):
    ind += PIV
    TREE[ind] += 1
    while True:
        ind >>= 1
        if ind == 0: return
        TREE[ind] += 1


def query(l, r):
    l += PIV; r += PIV;
    ret = 0
    while l <= r:
        if l & 1:
            ret += TREE[l]
            l += 1
        if not r & 1:
            ret += TREE[r]
            r -= 1
        l >>= 1; r >>= 1;
    return ret


if __name__ == "__main__":
    N = int(input())
    num2shrink = dict()
    nums = list(map(int, input().rstrip().split()))
    for i, num in enumerate(nums):
        num2shrink[num] = i

    querys = list(map(int, input().rstrip().split()))
    for i, q in enumerate(querys):
        querys[i] = num2shrink[q]

    tot = 0
    for q in querys:
        update(q)
        tot += query(q + 1, N - 1)

    print(tot)
