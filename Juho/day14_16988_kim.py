"""
input :
3 4
2 0 0 0
0 0 0 0
0 0 0 2

output :
1
"""
import sys
from itertools import combinations
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(cy, cx):
    global cnt; global success
    cnt += 1
    visited[cy][cx] = True
    for dy, dx in move:
        ny, nx = cy + dy, cx + dx
        if not (0 <= ny < R and 0 <= nx < C): continue
        if board[ny][nx] == 1: continue
        if visited[ny][nx]: continue
        if board[ny][nx] == 0:
            # 실패 -> 연결된 '2'자리는 모두 실패하는 자리
            # visited만 쭉 처리해서 다음번에 방문 안하게끔 한다.
            success = False

        visited[ny][nx] = True
        dfs(ny, nx)

    if success:
        return cnt
    else:
        return 0


def dfs_loop():
    global cnt; global success
    tmp_val = 0
    for r in range(R):
        for c in range(C):
            if visited[r][c]: continue
            if board[r][c] == 0 or board[r][c] == 1: continue

            cnt = 0
            success = True
            tmp_val += dfs(r, c)
    return tmp_val


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    board = []
    for _ in range(R):
        board.append(list(map(int, input().rstrip().split())))

    poses0 = []
    for r in range(R):
        for c in range(C):
            if board[r][c] == 0:
                poses0.append([r, c])

    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    cnt = 0
    max_val = 0
    for combi in list(combinations(poses0, 2)):
        for r, c in combi:
            board[r][c] = 1

        visited = [[False for _ in range(C)] for _ in range(R)]
        success = True
        max_val = max(max_val, dfs_loop())

        for r, c in combi:
            board[r][c] = 0

    print(max_val)
