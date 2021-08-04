"""
input :
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2

output :
5
"""

import sys
from itertools import combinations
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def find_vpos():
    for r in range(N):
        for c in range(N):
            if board[r][c] == 2:
                v_pos.append([r, c])


def bfs(combi):
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    ret = 0
    que = deque()
    for r, c in combi:
        que.append([r, c])
        visited[r][c] = 1
    while len(que) != 0:
        cy, cx = que.popleft()
        for dy, dx in move:
            ny, nx = cy + dy, cx + dx
            if not 0 <= ny < N: continue
            if not 0 <= nx < N: continue
            if board[ny][nx] == 1: continue
            if visited[ny][nx]: continue

            visited[ny][nx] = visited[cy][cx] + 1
            que.append([ny, nx])
            ret = max(ret, visited[ny][nx])

    if not entirely_covered(visited): ret = 100
    return ret


def entirely_covered(visited):
    for r in range(N):
        for c in range(N):
            if (visited[r][c] == 0) and (board[r][c] != 1):
                return False
    return True


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().rstrip().split())))

    v_pos = []
    find_vpos()

    min_val = 100
    combis = combinations(v_pos, M)
    for combi in combis:
        min_val = min(min_val, bfs(combi))

    if min_val == 100:
        print(-1)
    elif min_val == 0:
        print(0)
    else:
        print(min_val - 1)
