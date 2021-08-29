"""
input :
3
2
3
4

output :
55
220
715
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[0 for i in range(10)] for _ in range(N + 1)]

        for j in range(10):
            dp[1][j] = 1

        for i in range(2, N + 1):
            for k in range(10):
                for j in range(k, 10):
                    dp[i][k] += dp[i - 1][j]

        print(sum(dp[N]))
