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
    for j in range(c + 1, N):
        if board[r][j] == 'O' or board[r][j] == 'X':
            return
        bomb_spots[r][j] = False


def erase_bomb_spot_d(r, c):
    for i in range(r + 1, N):
        if board[i][c] == 'O' or board[i][c] == 'X':
            return
        bomb_spots[i][c] = False


def erase_bomb_spot_l(r, c):
    for j in range(c - 1, -1, -1):
        if board[r][j] == 'O' or board[r][j] == 'X':
            return
        bomb_spots[r][j] = False


def erase_bomb_spot_u(r, c):
    for i in range(r - 1, -1, -1):
        if board[i][c] == 'O' or board[i][c] == 'X':
            return
        bomb_spots[i][c] = False


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
