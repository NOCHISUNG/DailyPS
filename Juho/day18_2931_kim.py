"""
input :
3 7
.......
.M-.-Z.
.......

output :
2 4 -
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
right_accepted = {'1', '2', '-', '+', 'Z', 'M'}
down_accepted = {'1', '4', '|', '+', 'Z', 'M'}
left_accepted = {'3', '4', '-', '+', 'Z', 'M'}
upward_accepted = {'2', '3', '|', '+', 'Z', 'M'}


def kickout(y, x):
    if not (0 <= y < R and 0 <= x < C): return True
    if visited[y][x]: return True
    if board[y][x] == '.': return True
    return False


def bfs():
    global R, C
    global my, mx
    global zy, zx

    que = deque()
    que.append((my, mx, 'M'))
    visited[my][mx] = True
    while que:
        cy, cx, t = que.popleft()
        if (cy, cx) == (zy, zx):
            return True

        if t == '1':
            for dy, dx in [(0, 1), (1, 0)]:
                ny, nx = cy + dy, cx + dx
                if kickout(ny, nx): continue
                if (dy, dx) == (0, 1) and board[ny][nx] not in left_accepted: continue
                elif (dy, dx) == (1, 0) and board[ny][nx] not in upward_accepted: continue

                visited[ny][nx] = True
                que.append((ny, nx, board[ny][nx]))
        elif t == '2':
            for dy, dx in [(-1, 0), (0, 1)]:
                ny, nx = cy + dy, cx + dx
                if kickout(ny, nx): continue
                if (dy, dx) == (-1, 0) and board[ny][nx] not in down_accepted: continue
                elif (dy, dx) == (0, 1) and board[ny][nx] not in left_accepted: continue

                visited[ny][nx] = True
                que.append((ny, nx, board[ny][nx]))
        elif t == '3':
            for dy, dx in [(0, -1), (-1, 0)]:
                ny, nx = cy + dy, cx + dx
                if kickout(ny, nx): continue
                if (dy, dx) == (0, -1) and board[ny][nx] not in right_accepted: continue
                elif (dy, dx) == (-1, 0) and board[ny][nx] not in down_accepted: continue

                visited[ny][nx] = True
                que.append((ny, nx, board[ny][nx]))
        elif t == '4':
            for dy, dx in [(0, -1), (1, 0)]:
                ny, nx = cy + dy, cx + dx
                if kickout(ny, nx): continue
                if (dy, dx) == (0, -1) and board[ny][nx] not in right_accepted: continue
                elif (dy, dx) == (1, 0) and board[ny][nx] not in upward_accepted: continue

                visited[ny][nx] = True
                que.append((ny, nx, board[ny][nx]))
        elif t == '|':
            for dy, dx in [(-1, 0), (1, 0)]:
                ny, nx = cy + dy, cx + dx
                if kickout(ny, nx): continue
                if (dy, dx) == (-1, 0) and board[ny][nx] not in down_accepted: continue
                elif (dy, dx) == (1, 0) and board[ny][nx] not in upward_accepted: continue

                visited[ny][nx] = True
                que.append((ny, nx, board[ny][nx]))
        elif t == '-':
            for dy, dx in [(0, -1), (0, 1)]:
                ny, nx = cy + dy, cx + dx
                if kickout(ny, nx): continue
                if (dy, dx) == (0, -1) and board[ny][nx] not in right_accepted: continue
                elif (dy, dx) == (0, 1) and board[ny][nx] not in left_accepted: continue

                visited[ny][nx] = True
                que.append((ny, nx, board[ny][nx]))
        elif t == '+' or t == 'M':
            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ny, nx = cy + dy, cx + dx
                if kickout(ny, nx): continue
                if (dy, dx) == (0, 1) and board[ny][nx] not in left_accepted: continue
                elif (dy, dx) == (1, 0) and board[ny][nx] not in upward_accepted: continue
                elif (dy, dx) == (0, -1) and board[ny][nx] not in right_accepted: continue
                elif (dy, dx) == (-1, 0) and board[ny][nx] not in down_accepted: continue

                visited[ny][nx] = True
                que.append((ny, nx, board[ny][nx]))

    return False


def no_spare_pipe():
    for r in range(R):
        for c in range(C):
            t = board[r][c]
            if t == '.' or t == 'M' or t == 'Z': continue
            if t == '1':
                if (not 0 <= c + 1 < C) or (board[r][c + 1] not in left_accepted): return False
                if (not 0 <= r + 1 < R) or (board[r + 1][c] not in upward_accepted): return False
            elif t == '2':
                if (not 0 <= c + 1 < C) or (board[r][c + 1] not in left_accepted): return False
                if (not 0 <= r - 1 < R) or (board[r - 1][c] not in down_accepted): return False
            elif t == '3':
                if (not 0 <= c - 1 < C) or (board[r][c - 1] not in right_accepted): return False
                if (not 0 <= r - 1 < R) or (board[r - 1][c] not in down_accepted): return False
            elif t == '4':
                if (not 0 <= c - 1 < C) or (board[r][c - 1] not in right_accepted): return False
                if (not 0 <= r + 1 < R) or (board[r + 1][c] not in upward_accepted): return False
            elif t == '|':
                if (not 0 <= r - 1 < R) or (board[r - 1][c] not in down_accepted): return False
                if (not 0 <= r + 1 < R) or (board[r + 1][c] not in upward_accepted): return False
            elif t == '-':
                if (not 0 <= c - 1 < C) or (board[r][c - 1] not in right_accepted): return False
                if (not 0 <= c + 1 < C) or (board[r][c + 1] not in left_accepted): return False
            elif t == '+':
                if (not 0 <= c + 1 < C) or (board[r][c + 1] not in left_accepted): return False
                if (not 0 <= r + 1 < R) or (board[r + 1][c] not in upward_accepted): return False
                if (not 0 <= c - 1 < C) or (board[r][c - 1] not in right_accepted): return False
                if (not 0 <= r - 1 < R) or (board[r - 1][c] not in down_accepted): return False
    return True


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    board = []
    for _ in range(R):
        board.append(list(input().rstrip()))

    my, mx = -1, -1
    zy, zx = -1, -1
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'M':
                my, mx = r, c
            elif board[r][c] == 'Z':
                zy, zx = r, c

    pipe_types = ['1', '2', '3', '4', '|', '-', '+']
    for r in range(R):
        for c in range(C):
            for pipe_type in pipe_types:
                if board[r][c] != '.': continue

                visited = [[False for _ in range(C)] for _ in range(R)]
                tmp = board[r][c]
                board[r][c] = pipe_type
                if bfs() and no_spare_pipe():
                    print(r + 1, c + 1, pipe_type)
                    exit()
                else:
                    board[r][c] = tmp
