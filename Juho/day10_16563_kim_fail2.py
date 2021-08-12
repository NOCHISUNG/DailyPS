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


def r_move(ry, rx, by, bx):
    R_num = R_visited[ry][rx]
    if rx > bx:  # R을 먼저 최대한 오른쪽으로 붙인다.
        tmp_rx = rx
        while True:
            tmp_rx += 1

            # R이 이동하지 못하게 되는 조건들을 만나면, break
            if (not (0 <= tmp_rx < C)) or board[ry][tmp_rx] == '#' or R_visited[ry][tmp_rx]:
                tmp_rx -= 1
                break
            # R 목적지 도착
            if board[ry][tmp_rx] == 'O':
                break

        tmp_bx = bx
        while True:
            tmp_bx += 1
            # B가 이동하지 못하게 되는 조건들을 만나게 되면, break
            if (not (0 <= tmp_bx < C)) or board[by][tmp_bx] == '#':
                tmp_bx -= 1
                break

            if board[by][tmp_bx] == 'O':  # B 공이 빠졌으므로 실패로 return
                return -1, '_', '_', '_'
            # O가 아니고, R 공까지 도달
            if [by, tmp_bx] == [ry, tmp_rx]:
                tmp_bx -= 1
                break

    else:  # B를 먼저 최대한 오른쪽으로 붙인다.
        tmp_bx = bx
        while True:
            tmp_bx += 1
            if (not (0 <= tmp_bx < C)) or board[by][tmp_bx] == '#':
                tmp_bx -= 1
                break

            if board[by][tmp_bx] == 'O':
                return -1, '_', '_', '_'  # B 공이 빠졌으므로 실패로 return

        tmp_rx = rx
        while True:
            tmp_rx += 1
            if (not (0 <= tmp_rx < C)) or board[ry][tmp_rx] == '#' or [ry, tmp_rx] == [by, tmp_bx]:
                tmp_rx -= 1
                break

            # 이미 들른 곳에 재방문된 상황이라면, 실패로 판정함
            if R_visited[ry][tmp_rx]:
                return -1, '_', '_', '_'
            # B 공이 실패하지 않고, R 공이 무사히 목적지까지 도달
            if board[ry][tmp_rx] == 'O':
                break

    # R도, B도 성공적으로 이동할 수 있다면, R_visited에 기록
    for c in range(rx + 1, tmp_rx + 1):
        R_visited[ry][c] = R_num + 1
    return ry, tmp_rx, by, tmp_bx


def d_move(ry, rx, by, bx):
    R_num = R_visited[ry][rx]
    if ry > by:  # R을 먼저 최대한 아래쪽으로 붙인다.
        tmp_ry = ry
        while True:
            tmp_ry += 1

            # R이 이동하지 못하게 되는 조건들을 만나면, break
            if (not (0 <= tmp_ry < R)) or board[tmp_ry][rx] == '#' or R_visited[tmp_ry][rx]:
                tmp_ry -= 1
                break
            # R 목적지 도착
            if board[tmp_ry][rx] == 'O':
                break

        tmp_by = by
        while True:
            tmp_by += 1
            # B가 이동하지 못하게 되는 조건들을 만나게 되면, break
            if (not (0 <= tmp_by < R)) or board[tmp_by][bx] == '#':
                tmp_by -= 1
                break

            if board[tmp_by][bx] == 'O':  # B 공이 빠졌으므로 실패로 return
                return -1, '_', '_', '_'
            # O가 아니고, R 공까지 도달
            if [tmp_by, bx] == [tmp_ry, rx]:
                tmp_by -= 1
                break

    else:  # B를 먼저 최대한 아래쪽으로 붙인다.
        tmp_by = by
        while True:
            tmp_by += 1
            if (not (0 <= tmp_by < R)) or board[tmp_by][bx] == '#':
                tmp_by -= 1
                break

            if board[tmp_by][bx] == 'O':
                return -1, '_', '_', '_'  # B 공이 빠졌으므로 실패로 return

        tmp_ry = ry
        while True:
            tmp_ry += 1
            if (not (0 <= tmp_ry < R)) or board[tmp_ry][rx] == '#' or [tmp_ry, rx] == [tmp_by, bx]:
                tmp_ry -= 1
                break

            # 이미 들른 곳에 재방문된 상황이라면, 실패로 판정함
            if R_visited[tmp_ry][rx]:
                return -1, '_', '_', '_'
            # B 공이 실패하지 않고, R 공이 무사히 목적지까지 도달
            if board[tmp_ry][rx] == 'O':
                break

    # R도, B도 성공적으로 이동할 수 있다면, R_visited에 기록
    for r in range(ry + 1, tmp_ry + 1):
        R_visited[r][rx] = R_num + 1
    return tmp_ry, rx, tmp_by, bx


def l_move(ry, rx, by, bx):
    R_num = R_visited[ry][rx]
    if rx < bx:  # R을 먼저 최대한 왼쪽으로 붙인다.
        tmp_rx = rx
        while True:
            tmp_rx -= 1

            # R이 이동하지 못하게 되는 조건들을 만나면, break
            if (not (0 <= tmp_rx < C)) or board[ry][tmp_rx] == '#' or R_visited[ry][tmp_rx]:
                tmp_rx += 1
                break
            # R 목적지 도착
            if board[ry][tmp_rx] == 'O':
                break

        tmp_bx = bx
        while True:
            tmp_bx -= 1
            # B가 이동하지 못하게 되는 조건들을 만나게 되면, break
            if (not (0 <= tmp_bx < C)) or board[by][tmp_bx] == '#':
                tmp_bx += 1
                break

            if board[by][tmp_bx] == 'O':  # B 공이 빠졌으므로 실패로 return
                return -1, '_', '_', '_'
            # O가 아니고, R 공까지 도달
            if [by, tmp_bx] == [ry, tmp_rx]:
                tmp_bx += 1
                break

    else:  # B를 먼저 최대한 왼쪽으로 붙인다.
        tmp_bx = bx
        while True:
            tmp_bx -= 1
            if (not (0 <= tmp_bx < C)) or board[by][tmp_bx] == '#':
                tmp_bx += 1
                break

            if board[by][tmp_bx] == 'O':
                return -1, '_', '_', '_'  # B 공이 빠졌으므로 실패로 return

        tmp_rx = rx
        while True:
            tmp_rx -= 1
            if (not (0 <= tmp_rx < C)) or board[ry][tmp_rx] == '#' or [ry, tmp_rx] == [by, tmp_bx]:
                tmp_rx += 1
                break

            # 이미 들른 곳에 재방문된 상황이라면, 실패로 판정함
            if R_visited[ry][tmp_rx]:
                return -1, '_', '_', '_'
            # B 공이 실패하지 않고, R 공이 무사히 목적지까지 도달
            if board[ry][tmp_rx] == 'O':
                break

    # R도, B도 성공적으로 이동할 수 있다면, R_visited에 기록
    for c in range(tmp_rx, rx):
        R_visited[ry][c] = R_num + 1
    return ry, tmp_rx, by, tmp_bx


def u_move(ry, rx, by, bx):
    R_num = R_visited[ry][rx]
    if ry < by:  # R을 먼저 최대한 위쪽으로 붙인다.
        tmp_ry = ry
        while True:
            tmp_ry -= 1

            # R이 이동하지 못하게 되는 조건들을 만나면, break
            if (not (0 <= tmp_ry < R)) or board[tmp_ry][rx] == '#' or R_visited[tmp_ry][rx]:
                tmp_ry += 1
                break
            # R 목적지 도착
            if board[tmp_ry][rx] == 'O':
                break

        tmp_by = by
        while True:
            tmp_by -= 1
            # B가 이동하지 못하게 되는 조건들을 만나게 되면, break
            if (not (0 <= tmp_by < R)) or board[tmp_by][bx] == '#':
                tmp_by += 1
                break

            if board[tmp_by][bx] == 'O':  # B 공이 빠졌으므로 실패로 return
                return -1, '_', '_', '_'
            # O가 아니고, R 공까지 도달
            if [tmp_by, bx] == [tmp_ry, rx]:
                tmp_by += 1
                break

    else:  # B를 먼저 최대한 위쪽으로 붙인다.
        tmp_by = by
        while True:
            tmp_by -= 1
            if (not (0 <= tmp_by < R)) or board[tmp_by][bx] == '#':
                tmp_by += 1
                break

            if board[tmp_by][bx] == 'O':
                return -1, '_', '_', '_'  # B 공이 빠졌으므로 실패로 return

        tmp_ry = ry
        while True:
            tmp_ry -= 1
            if (not (0 <= tmp_ry < R)) or board[tmp_ry][rx] == '#' or [tmp_ry, rx] == [tmp_by, bx]:
                tmp_ry += 1
                break

            # 이미 들른 곳에 재방문된 상황이라면, 실패로 판정함
            if R_visited[tmp_ry][rx]:
                return -1, '_', '_', '_'
            # B 공이 실패하지 않고, R 공이 무사히 목적지까지 도달
            if board[tmp_ry][rx] == 'O':
                break

    # R도, B도 성공적으로 이동할 수 있다면, R_visited에 기록
    for r in range(tmp_ry, ry):
        R_visited[r][rx] = R_num + 1
    return tmp_ry, rx, tmp_by, bx


def bfs():
    que = deque()
    que.append([sRy, sRx, sBy, sBx])
    R_visited[sRy][sRx] = 1

    while que:
        cry, crx, cby, cbx = que.popleft()
        for move_fun in move:
            nry, nrx, nby, nbx = move_fun(cry, crx, cby, cbx)
            if nry == -1:  # means fail
                continue
            if [nry, nrx, nby, nbx] == [cry, crx, cby, cbx]:  # means no change
                continue

            if [nry, nrx] == [Oy, Ox] and [nby, nbx] != [Oy, Ox]:
                # R은 O에 도착했으나, B는 O에 도착하지 않은 해피한 상황을 만나게 되면 -> 성공
                return

            que.append([nry, nrx, nby, nbx])


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
    bfs()

    if R_visited != 0:
        print(R_visited[Oy][Ox] - 1)
    else:
        print(-1)
