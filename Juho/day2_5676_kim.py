"""
input :
4 6
-2 6 0 -1
C 1 10
P 1 4
C 3 7
P 2 2
C 4 -5
P 1 4
5 9
1 5 -2 4 3
P 1 2
P 1 5
C 4 -5
P 1 5
P 4 5
C 3 0
P 1 5
C 4 -5
C 4 -5

output :
0+-
+-+-0
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
PIV = 1 << 17
tree = [1 for _ in range(2 * PIV)]


def update(ind, val):
    ind += PIV
    if val > 0: val = 1
    elif val < 0: val = -1

    tree[ind] = val
    while True:
        ind >>= 1
        if ind == 0: return

        tree[ind] = tree[2 * ind] * tree[2 * ind + 1]


def query(l, r):
    l += PIV; r += PIV;
    ret = 1
    while l <= r:
        if l & 1:
            ret *= tree[l]
            l += 1
        if not r & 1:
            ret *= tree[r]
            r -= 1
        l >>= 1; r >>= 1;
    return ret


if __name__ == "__main__":
    try:
        while True:
            N, K = map(int, input().rstrip().split())
            nums = list(map(int, input().rstrip().split()))
            ind = 1
            for num in nums:
                update(ind, num)
                ind += 1

            for _ in range(K):
                cmd = list(input().rstrip().split())
                cmd[1], cmd[2] = int(cmd[1]), int(cmd[2])
                if cmd[0] == 'C':
                    update(cmd[1], cmd[2])
                elif cmd[0] == 'P':
                    ans = query(cmd[1], cmd[2])
                    if ans == 0:
                        print(0, end='')
                    elif ans < 0:
                        print('-', end='')
                    else:
                        print('+', end='')
            print()
    except:
        pass
