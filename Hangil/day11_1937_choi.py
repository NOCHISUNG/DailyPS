import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 1
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < n and 0 <= y1 < n and table[x][y] < table[x1][y1]:
            dp[x][y] = max(dp[x][y], dfs(x1, y1)+1)

    return dp[x][y]
        

n = int(input())
table = [list(map(int, input().split())) for x in range(n)]
dp = [[-1 for y in range(n)] for x in range(n)]

ans = 0
for x in range(n):
    for y in range(n):
        ans = max(ans, dfs(x, y))

print(ans)
