"""
input :
7 7
#######
#...RB#
#.#####
#.....#
#####.#
#O....#
#######

output :
5
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def move_ball(y, x, i):
    mov_cnt = 0
    dy = move[i][0]
    dx = move[i][1]
    while True:
        y += dy
        x += dx
        mov_cnt += 1

        if board[y][x] == '#':
            y -= dy
            x -= dx
            mov_cnt -= 1
            break
        elif board[y][x] == 'O':
            break

    return y, x, mov_cnt


def bfs():
    que = deque()
    que.append([sry, srx, sby, sbx, 0])
    visited[sry][srx][sby][sbx] = True

    while que:
        cry, crx, cby, cbx, mov_cnt = que.popleft()
        for i in range(4):
            nry, nrx, rmov_num = move_ball(cry, crx, i)
            nby, nbx, bmov_num = move_ball(cby, cbx, i)

            if board[nby][nbx] == 'O': continue
            if board[nry][nrx] == 'O':
                print(mov_cnt + 1)
                return

            if [nry, nrx] == [nby, nbx]:
                if rmov_num > bmov_num:
                    nry -= move[i][0]
                    nrx -= move[i][1]
                else:
                    nby -= move[i][0]
                    nbx -= move[i][1]

            if not visited[nry][nrx][nby][nbx]:
                visited[nry][nrx][nby][nbx] = True
                que.append([nry, nrx, nby, nbx, mov_cnt + 1])

    print(-1)
    return


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    board = []
    for _ in range(R):
        board.append(list(input().rstrip()))

    for r in range(R):
        for c in range(C):
            if board[r][c] == 'R':
                sry, srx = r, c
            elif board[r][c] == 'B':
                sby, sbx = r, c
            elif board[r][c] == 'O':
                Oy, Ox = r, c

    visited = [[[[False for _ in range(C)] for _ in range(R)] for _ in range(C)] for _ in range(R)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    bfs()
