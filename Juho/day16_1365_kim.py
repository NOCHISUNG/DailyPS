"""
input :
4
2 3 4 1

output :
1
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
PIV = 1 << 17
TREE = [0 for _ in range(2 * PIV)]


def update(ind, val):
    ind += PIV
    TREE[ind] = val
    while True:
        ind >>= 1
        if ind == 0: break
        TREE[ind] = max(TREE[2 * ind], TREE[2 * ind + 1])


def query(l, r):
    l += PIV; r += PIV;
    ret = 0
    while l <= r:
        if l & 1:
            ret = max(ret, TREE[l])
            l += 1
        if not r & 1:
            ret = max(ret, TREE[r])
            r -= 1
        l >>= 1; r >>= 1
    return ret


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    LIS = 0
    for num in nums:
        max_val = query(1, num - 1)
        update(num, max_val + 1)
        LIS = max(LIS, max_val + 1)
    print(N - LIS)