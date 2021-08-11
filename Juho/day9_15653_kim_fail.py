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


def l_move(ry, rx, by, bx):
    R_num = R_visited[ry][rx]

    if rx < bx:  # R을 먼저 보냄
        while True:
            rx -= 1
            if not (0 <= rx < C):
                rx += 1
                break
            if board[ry][rx] == '#':
                rx += 1
                break
            if R_visited[ry][rx]:
                rx += 1
                break
            R_visited[ry][rx] = R_num + 1

            if board[ry][rx] == 'O':
                break
        while True:
            bx -= 1
            if not (0 <= bx < C):
                bx += 1
                break
            if board[by][bx] == '#':
                bx += 1
                break
            if board[by][bx] == 'O':
                return Oy, Ox, Oy, Ox  # B 공이 빠졌으므로 실패로 return

            if [by, bx] == [ry, rx]:  # R 공까지 도달
                bx += 1
                break

    else:  # B를 먼저 보냄
        while True:
            bx -= 1
            if not (0 <= bx < C):
                bx += 1
                break
            if board[by][bx] == '#':
                bx += 1
                break

            if board[by][bx] == 'O':
                return Oy, Ox, Oy, Ox  # B 공이 빠졌으므로 실패로 return

        while True:
            rx -= 1
            if not (0 <= rx < C):
                rx += 1
                break
            if board[ry][rx] == '#' or [ry, rx] == [by, bx]:
                rx += 1
                break
            if R_visited[ry][rx]:
                rx += 1
                break
            R_visited[ry][rx] = R_num + 1

            if board[ry][rx] == 'O':
                break

    return ry, rx, by, bx


def d_move(ry, rx, by, bx):
    R_num = R_visited[ry][rx]
    if ry > by:  # R 먼저 보냄
        while True:
            ry += 1
            if not (0 <= ry < R):
                ry -= 1
                break
            if board[ry][rx] == '#':
                ry -= 1
                break
            if R_visited[ry][rx]:
                ry -= 1
                break
            R_visited[ry][rx] = R_num + 1

            if board[ry][rx] == 'O':
                break
        while True:
            by += 1
            if not (0 <= by < R):
                by -= 1
                break
            if board[by][bx] == '#':
                by -= 1
                break

            if board[by][bx] == 'O':
                return Oy, Ox, Oy, Ox  # B 공이 빠졌으므로 실패로 return

            if [by, bx] == [ry, rx]:
                by -= 1
                break

    else:  # B을 먼저 보냄
        while True:
            by += 1
            if not (0 <= bx < R):
                by -= 1
                break
            if board[by][bx] == '#':
                by -= 1
                break

            if board[by][bx] == 'O':
                return Oy, Ox, Oy, Ox  # B 공이 빠졌으므로 실패로 return

        while True:
            ry += 1
            if not (0 <= ry < R):
                ry -= 1
                break
            if board[ry][rx] == '#' or [ry, rx] == [by, bx]:
                ry -= 1
                break
            if R_visited[ry][rx]:
                ry -= 1
                break
            R_visited[ry][rx] = R_num + 1

            if board[ry][rx] == 'O':
                break

    return ry, rx, by, bx


def r_move(ry, rx, by, bx):
    R_num = R_visited[ry][rx]

    if rx > bx:  # R을 먼저 보냄
        while True:
            rx += 1
            if not (0 <= rx < C):
                rx -= 1
                break
            if board[ry][rx] == '#':
                rx -= 1
                break
            if R_visited[ry][rx]:
                rx -= 1
                break
            R_visited[ry][rx] = R_num + 1

            if board[ry][rx] == 'O':
                break
        while True:
            bx == 1
            if not (0 <= bx < C):
                bx -= 1
                break
            if board[by][bx] == '#':
                bx -= 1
                break

            if board[by][bx] == 'O':
                return Oy, Ox, Oy, Ox  # B 공이 빠졌으므로 실패로 return

            if [by, bx] == [ry, rx]:
                bx -= 1
                break

    else:  # B를 먼저 보냄
        while True:
            bx += 1
            if not (0 <= bx < C):
                bx -= 1
                break
            if board[by][bx] == '#':
                bx -= 1
                break
            if board[by][bx] == 'O':
                return Oy, Ox, Oy, Ox  # B 공이 빠졌으므로 실패로 return

        while True:
            rx += 1
            if not (0 <= rx < C):
                rx -= 1
                break
            if board[ry][rx] == '#' or [ry, rx] == [by, bx]:
                rx -= 1
                break
            if R_visited[ry][rx]:
                rx -= 1
                break
            R_visited[ry][rx] = R_num + 1

            if board[ry][rx] == 'O':
                break

    return ry, rx, by, bx


def u_move(ry, rx, by, bx):
    R_num = R_visited[ry][rx]
    if ry < by:  # R 먼저 보냄
        while True:
            ry -= 1
            if not (0 <= ry < R):
                ry += 1
                break
            if board[ry][rx] == '#':
                ry += 1
                break
            if R_visited[ry][rx]:
                ry += 1
                break
            R_visited[ry][rx] = R_num + 1
        while True:
            by -= 1
            if not (0 <= by < R):
                by += 1
                break
            if board[by][bx] == '#' or [by, bx] == [ry, rx]:
                by += 1
                break

    else:  # B을 먼저 보냄
        while True:
            by -= 1
            if not (0 <= bx < R):
                by += 1
                break
            if board[by][bx] == '#':
                by += 1
                break

        while True:
            ry -= 1
            if not (0 <= ry < R):
                ry += 1
                break
            if board[ry][rx] == '#' or [ry, rx] == [by, bx]:
                ry += 1
                break
            if R_visited[ry][rx]:
                ry += 1
                break
            R_visited[ry][rx] = R_num + 1

    return ry, rx, by, bx


def bfs():
    que = deque()
    que.append([sRy, sRx, sBy, sBx])
    R_visited[sRy][sRx] = 1

    while que:
        cry, crx, cby, cbx = que.popleft()
        R_num = R_visited[cry][crx]
        for i, mov_fun in enumerate(move):
            if i == 0 and crx + 1 < C and R_visited[cry][crx + 1]:
                continue
            elif i == 1 and cry + 1 < R and R_visited[cry + 1][crx]:
                continue
            elif i == 2 and crx - 1 > 0 and R_visited[cry][crx - 1]:
                continue
            elif i == 3 and cry - 1 > 0 and R_visited[cry - 1][crx]:
                continue

            nry, nrx, nby, nbx = mov_fun(cry, crx, cby, cbx)
            if [nry, nrx] == [Oy, Ox] and [nby, nbx] != [Oy, Ox]:
                return True
            elif [nry, nrx] == [nby, nbx] == [Oy, Ox]:
                continue
            if [cry, crx, cby, cbx] == [nry, nrx, nby, nbx]:
                R_visited[cry][crx] = R_num
                continue
            que.append([nry, nrx, nby, nbx])
    return False


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    board = []
    for _ in range(R):
        board.append(list(input().rstrip()))

    for r in range(R):
        for c in range(C):
            if board[r][c] == 'R':
                sRy, sRx = r, c
            elif board[r][c] == 'B':
                sBy, sBx = r, c
            elif board[r][c] == 'O':
                Oy, Ox = [r, c]

    move = [r_move, d_move, l_move, u_move]
    R_visited = [[0 for _ in range(C)] for _ in range(R)]
    if bfs():
        print(R_visited[Oy][Ox] - 1)
    else:
        print(-1)
