import sys

input = sys.stdin.readline


def go(idx, end):
    if dp[idx][end] != -1:
        return dp[idx][end]

    ret = 0
    for x in range(end + 1):
        ret += go(idx - 1, x)

    dp[idx][end] = ret
    return ret


# dp[x][y] x자리에 y로 끝나는 수
dp = [[-1 for y in range(10)] for x in range(65)]
for x in range(10):
    dp[1][x] = 1

t = int(input())
for _ in range(t):
    n = int(input())

    ans = 0
    for x in range(10):
        ans += go(n, x)

    print(ans)
