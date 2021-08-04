import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check():
    for x in range(n):
        for y in range(n):
            if new_table[x][y] == 0:
                return False
    return True


def time():
    M = 0
    for tt in new_table:
        M = max(M, max(tt))
    return M-1
            

n, m = map(int, input().split())
table = [list(map(int, input().split())) for x in range(n)]
ans = sys.maxsize

virus = []
for x in range(n):
    for y in range(n):
        if table[x][y] == 2:
            virus.append((x,y))
            table[x][y] = 0

for combi in combinations(virus, m):
    new_table = deepcopy(table)

    dq = deque()
    for x, y in combi:
        new_table[x][y] = 1
        dq.append((x, y, 1))

    while dq:
        x, y, cnt = dq.popleft()

        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]

            if 0 <= x1 < n and 0 <= y1 < n and new_table[x1][y1] == 0:
                new_table[x1][y1] = cnt+1
                dq.append((x1, y1, cnt+1))

    if check():
        ans = min(ans, time())

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
            
