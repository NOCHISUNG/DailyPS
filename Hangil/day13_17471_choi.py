import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline


def check(arr):
    dq = deque()
    dq.append(arr[0])
    visit = [0 for x in range(n)]
    visit[arr[0]] = 1

    while dq:
        here = dq.popleft()

        for there in range(n):
            if table[here][there] != 0 and there in arr and visit[there] == 0:
                visit[there] = 1
                dq.append(there)

    if sum(visit) == len(arr):
        return True
    return False


def total(arr):
    ret = 0
    for x in arr:
        ret += people[x]

    return ret


n = int(input())
people = list(map(int, input().split()))
table = [[0 for y in range(n)] for x in range(n)]

for x in range(n):
    temp = list(map(int, input().split()))
    for y in temp[1:]:
        table[x][y - 1] = 1
        table[y - 1][x] = 1

ans = sys.maxsize
arr = [x for x in range(n)]
for k in range(1, n // 2 + 1):
    for com in combinations(arr, k):
        A = list(com)
        B = []
        for x in range(n):
            if x not in A:
                B.append(x)

        if check(A) and check(B):
            sumA = total(A)
            sumB = total(B)
            ans = min(ans, abs(sumA - sumB))

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)