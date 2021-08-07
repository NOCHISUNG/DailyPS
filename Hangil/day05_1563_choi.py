import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def go(day, late, absent):
    if late == 2:
        return 0
    if absent == 3:
        return 0

    if day == n:
        return 1

    ret = dp[day][late][absent]
    if ret != -1:
        return ret

    ret = go(day+1, late+1, 0) + go(day+1, late, absent+1) + go(day+1, late, 0)

    dp[day][late][absent] = ret%1000000

    return dp[day][late][absent]


n = int(input())
#dp[x][y][z] x일 y지각 z결석
dp = [[[-1 for z in range(3)] for y in range(2)] for x in range(n)]

print(go(0, 0, 0))
