"""
input :
5
...XO
..XOO
...XO
O....
OXX..

output:
.B.XO
..XOO
..BXO
O....
OXX..
"""
import sys
sys.stdin = open("cmake-build-debug/input.txt", "r")
input = sys.stdin.readline


def erase_bomb_spot_r(r, c):
    c_cpy = c
    while True:
        c += 1
        if c == N:
            for j in range(c_cpy + 1, c):
                bomb_spots[r][j] = False
            return True
        if board[r][c] == 'O' or board[r][c] == 'X':
            for j in range(c_cpy + 1, c):
                bomb_spots[r][j] = False
            return True


def erase_bomb_spot_d(r, c):
    r_cpy = r
    while True:
        r += 1
        if r == N:
            for i in range(r_cpy + 1, r):
                bomb_spots[i][c] = False
            return True
        if board[r][c] == 'O' or board[r][c] == 'X':
            for i in range(r_cpy + 1, r):
                bomb_spots[i][c] = False
            return True


def erase_bomb_spot_l(r, c):
    c_cpy = c
    while True:
        c -= 1
        if c == -1:
            for j in range(c_cpy - 1, c, -1):
                bomb_spots[r][j] = False
            return True
        if board[r][c] == 'O' or board[r][c] == 'X':
            for j in range(c_cpy - 1, c, -1):
                bomb_spots[r][j] = False
            return True


def erase_bomb_spot_u(r, c):
    r_cpy = r
    while True:
        r -= 1
        if r == -1:
            for i in range(r_cpy - 1, r, -1):
                bomb_spots[i][c] = False
            return True
        if board[r][c] == 'O' or board[r][c] == 'X':
            for i in range(r_cpy - 1, r, -1):
                bomb_spots[i][c] = False
            return True


if __name__ == "__main__":
    N = int(input())
    board = []
    bomb_spots = [[True for _ in range(N)] for _ in range(N)]
    for _ in range(N):
        tmp = list(input().rstrip())
        board.append(tmp)

    for r in range(N):
        for c in range(N):
            if board[r][c] == 'O' or board[r][c] == 'X':
                bomb_spots[r][c] = False

    funs = [erase_bomb_spot_r, erase_bomb_spot_d, erase_bomb_spot_l, erase_bomb_spot_u]
    for r in range(N):
        for c in range(N):
            if board[r][c] == 'O':
                for fun in funs:
                    fun(r, c)

    for r in range(N):
        for c in range(N):
            if bomb_spots[r][c]:
                print('B', end='')
            else:
                print(board[r][c], end='')
        print()
