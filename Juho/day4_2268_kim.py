"""
input :
3 5
0 1 3
1 1 2
1 2 3
0 2 3
0 1 3

output :
0
3
5
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
PIV = 1 << 20
TREE = [0 for _ in range(2 * PIV)]


def update(ind, x):
    ind += PIV
    TREE[ind] = x

    while True:
        ind >>= 1
        if ind == 0: return

        TREE[ind] = TREE[2 * ind] + TREE[2 * ind + 1]


def query(l, r):
    if l > r: l, r = r, l

    l += PIV; r += PIV
    ret = 0
    while l <= r:
        if l & 1:
            ret += TREE[l]; l += 1;
        if not r & 1:
            ret += TREE[r]; r -= 1;
        l >>= 1; r >>= 1;
    return ret


if __name__ == "__main__":
    N, Q = map(int, input().rstrip().split())
    for _ in range(Q):
        line = list(map(int, input().rstrip().split()))
        if line[0] == 0:
            print(query(line[1], line[2]))
        else:
            update(line[1], line[2])
