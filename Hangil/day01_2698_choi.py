import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def go(n, k, e):
    if k == -1:
        return 0
    if n < k+1:
        return 0
    if n == 1:
        dp[n][k][e] = 1
        return 1
    
    if dp[n][k][e] != -1:
        return dp[n][k][e]

    temp= 0
    if e == 1:
        temp += go(n-1, k-1, 1) + go(n-1, k, 0)
    elif e == 0:
        temp += go(n-1, k, 0) + go(n-1, k, 1)

    dp[n][k][e] = temp
    return temp


#dp[x][y][z] 수열크기 x 인접한 비트의 개수 y 끝 숫자 z
dp = [[[-1 for z in range(2)] for y in range(101)] for x in range(101)]


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(go(n, k, 0)+go(n, k, 1))
