import sys
from itertools import combinations
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if table[x][y] == 0:
        return 401
    if table[x][y] == 1:
        return 0
    if visit[x][y] == 1:
        return 0

    visit[x][y] = 1
    ret = 1
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]

        ret += dfs(x1, y1)

    return ret


def go():
    global ans
    die = 0    
    for x in range(n+2):
        for y in range(m+2):
            if table[x][y] == 2 and visit[x][y] == 0:
                kill = dfs(x, y)
                if kill < 401:
                    die += kill

    ans = max(ans, die)


n, m = map(int, input().split())
table = [[1 for x in range(m+2)]]
for x in range(n):
    table.append([1] + list(map(int, input().split())) + [1])
table.append([1 for x in range(m+2)])

stones = []
for x in range(n+2):
    for y in range(m+2):
        if table[x][y] == 0:
            stones.append((x, y))

ans = 0
for com in combinations(stones, 2):
    visit = [[0 for y in range(m+2)] for x in range(n+2)]
    table[com[0][0]][com[0][1]] = 1
    table[com[1][0]][com[1][1]] = 1
    go()
    table[com[0][0]][com[0][1]] = 0
    table[com[1][0]][com[1][1]] = 0

print(ans)
