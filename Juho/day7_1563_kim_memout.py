"""
input :
4

output :
43
"""

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
MOD = 1000000


def recur(day, attendance, late, absent):
    if late == 2:
        return 0
    if absent == 3:
        return 0
    if day == N:
        return 1
    if dp[day][attendance][late][absent] != 0:
        return dp[day][attendance][late][absent]

    dp[day][attendance][late][absent] = \
        recur(day + 1, attendance + 1, late, 0) + \
        recur(day + 1, attendance, late + 1, 0) + \
        recur(day + 1, attendance, late, absent + 1)

    dp[day][attendance][late][absent] %= MOD
    return dp[day][attendance][late][absent]


if __name__ == "__main__":
    N = int(input())

    dp = [[[[0 for _ in range(3)] for _ in range(2)] for _ in range(N + 1)] for _ in range(N + 1)]
    print(recur(0, 0, 0, 0) % MOD)
