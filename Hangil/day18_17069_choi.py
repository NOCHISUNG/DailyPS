import sys
input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for x in range(n)]

dp = [[[0 for k in range(3)] for y in range(n)] for x in range(n)]
#dp[x][y][k] x,y좌표에 k방향으로 오는 방법의 수
#k 0 : 가로, 1 : 세로, 2 : 대각


for y in range(1, n):
    if table[0][y] == 1:
        break
    dp[0][y][1] = 1

for x in range(1, n):
    for y in range(2, n):
        if table[x][y] == 1:
            continue
        #k 0
        dp[x][y][0] = dp[x-1][y][0] + dp[x-1][y][2]
        #k 1
        dp[x][y][1] = dp[x][y-1][1] + dp[x][y-1][2]
        #k 2
        if table[x-1][y] == 0 and table[x][y-1] == 0:
            dp[x][y][2] = dp[x-1][y-1][0] + dp[x-1][y-1][1] + dp[x-1][y-1][2]

print(sum(dp[n-1][n-1]))
