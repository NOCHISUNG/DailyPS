"""
input :
3
0 0 0
0 0 0
0 0 0

output :
1
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def chk(y, x):
    global N
    if not (0 <= y <= N and 0 <= x <= N): return False
    if board[y][x] == 1: return False
    return True


if __name__ == "__main__":
    N = int(input())
    board = [[0 for _ in range(N + 1)]]
    for _ in range(N):
        board.append([0] + list(map(int, input().rstrip().split())))

    dp = [[[0 for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(3)]
    dp[0][1][2] = 1
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            if board[y][x]: continue

            if chk(y, x) and chk(y, x - 1):
                dp[0][y][x] += dp[0][y][x - 1] + dp[2][y][x - 1]
            if chk(y, x) and chk(y - 1, x):
                dp[1][y][x] += dp[1][y - 1][x] + dp[2][y - 1][x]
            if chk(y, x) and chk(y - 1, x) and chk(y, x - 1) and chk(y - 1, x - 1):
                dp[2][y][x] += dp[0][y - 1][x - 1] + dp[1][y - 1][x - 1] + dp[2][y - 1][x - 1]

    print(dp[0][N][N] + dp[1][N][N] + dp[2][N][N])
