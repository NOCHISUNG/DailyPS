"""
input :
3
5 17
*****************
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*
*****************
cz
5 11
*.*********
*...*...*x*
*X*.*.*.*.*
*$*...*...*
***********
0
7 7
*ABCDE*
X.....F
W.$$$.G
V.$$$.H
U.$$$.J
T.....K
*SQPML*
irony

output :
3
1
0
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs(starts):
    global tot
    global R, C
    doc_find_flag = key_find_flag = False
    que = deque()
    visited = [[False for _ in range(C)] for _ in range(R)]
    for sy, sx in starts:
        que.append((sy, sx))
        visited[sy][sx] = True

    while que:
        cy, cx = que.popleft()
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = cy + dy, cx + dx
            if not (0 <= ny < R and 0 <= nx < C): continue
            if visited[ny][nx]: continue
            if board[ny][nx] == '*': continue

            if board[ny][nx].isupper():
                if board[ny][nx].lower() in key_set:
                    board[ny][nx] = '.'
                else:
                    continue

            elif board[ny][nx].islower():
                if board[ny][nx] not in key_set:
                    for y, x in upperchar2sidepos[board[ny][nx].upper()]:
                        board[y][x] = '.'
                        starts.add((y, x))
                    key_set.add(board[ny][nx])
                    key_find_flag = True
                board[ny][nx] = '.'

            elif board[ny][nx] == '$':
                board[ny][nx] = '.'
                doc_find_flag = True
                tot += 1

            visited[ny][nx] = True
            que.append((ny, nx))

            # for r in range(R):
            #     for c in range(C):
            #         print(board[r][c], end=' ')
            #     print()
            # print()

    if doc_find_flag or key_find_flag:
        return True
    else:
        return False


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        R, C = map(int, input().rstrip().split())
        board = list()
        for _ in range(R):
            board.append(list(input().rstrip()))
        key_set = set(input().rstrip())

        upperchar2sidepos = dict()
        for i in range(65, 91):
            upperchar2sidepos[chr(i)] = list()

        tot = 0
        starts = set()
        for r in range(R):
            for c in range(C):
                if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                    if board[r][c].islower():
                        key_set.add(board[r][c])
                        board[r][c] = '.'
                    if board[r][c] == '.':
                        starts.add((r, c))
                    if board[r][c] == '$':
                        starts.add((r, c))
                        tot += 1
                        board[r][c] = '.'
        for r in range(R):
            for c in range(C):
                if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                    if board[r][c].isupper():
                        if board[r][c].lower() in key_set:
                            board[r][c] = '.'
                            starts.add((r, c))
                        else:
                            upperchar2sidepos[board[r][c]].append((r, c))  # 이 position은 혹시 빌딩 안에서 키를 찾으면 열수가 있음
        # print(upper2pos)
        while True:
            if not bfs(starts):
                break

        print(tot)
