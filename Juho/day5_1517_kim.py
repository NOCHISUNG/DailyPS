"""
input :
3
3 2 1

output :
3
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
PIV = 1 << 20
TREE = [0 for _ in range(2 * PIV)]


def update(ind):
    ind += PIV

    TREE[ind] += 1
    while True:
        ind >>= 1
        if ind == 0: return
        TREE[ind] += 1


def query(l, r):
    l += PIV; r += PIV
    ret = 0
    while l <= r:
        if l & 1:
            ret += TREE[l]; l += 1
        if not r & 1:
            ret += TREE[r]; r -= 1
        l >>= 1; r >>= 1;
    return ret


def comp(arr):
    return arr[1]


if __name__ == "__main__":
    N = int(input())

    # 좌표압축
    nums = list(map(int, input().rstrip().split()))
    num2i = [[num, i] for i, num in enumerate(nums)]

    # relabeling
    num2i.sort()
    comp_num = 0
    for i in range(N - 1):
        if num2i[i][0] != num2i[i + 1][0]:
            num2i[i][0] = comp_num
            comp_num += 1
        else:
            num2i[i][0] = comp_num
    num2i[N - 1][0] = comp_num

    # restore to original
    num2i.sort(key= lambda x: comp(x))

    # print answer
    tot = 0
    for num, _ in num2i:
        update(num)
        tot += query(num + 1, N)
    print(tot)
