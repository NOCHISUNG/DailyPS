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


def bomb_spot_chk(r, c, direction):
    if direction == 'r':
        c_cpy = c
        while True:
            c += 1
            if c == N:
                for j in range(c_cpy + 1, c):
                    chk[r][j] = True
                return True
            if board[r][c] == 'O':
                return False
            if board[r][c] == 'X':
                for j in range(c_cpy + 1, c):
                    chk[r][j] = True
                return True

    elif direction == 'd':
        r_cpy = r
        while True:
            r += 1
            if r == N:
                for i in range(r_cpy + 1, r):
                    chk[i][c] = True
                return True
            if board[r][c] == 'O':
                return False
            if board[r][c] == 'X':
                for i in range(r_cpy + 1, r):
                    chk[i][c] = True
                return True

    elif direction == 'l':
        c_cpy = c
        while True:
            c -= 1
            if c == -1:
                for j in range(c_cpy - 1, c, -1):
                    chk[r][j] = True
                return True
            if board[r][c] == 'O':
                return False
            if board[r][c] == 'X':
                for j in range(c_cpy - 1, c, -1):
                    chk[r][j] = True
                return True

    elif direction == 'u':
        r_cpy = r
        while True:
            r -= 1
            if r == -1:
                for i in range(r_cpy - 1, r, -1):
                    chk[i][c] = True
                return True
            if board[r][c] == 'O':
                return False
            if board[r][c] == 'X':
                for i in range(r_cpy - 1, r, -1):
                    chk[i][c] = True
                return True


def erase_bomb_spot(r, c, direction):
    if direction == 'r':
        c_cpy = c
        while True:
            c += 1
            if c == N:
                for j in range(c_cpy + 1, c):
                    chk[r][j] = False
                return True
            if board[r][c] == 'O' or board[r][c] == 'X':
                for j in range(c_cpy + 1, c):
                    chk[r][j] = False
                return True

    elif direction == 'd':
        r_cpy = r
        while True:
            r += 1
            if r == N:
                for i in range(r_cpy + 1, r):
                    chk[i][c] = False
                return True
            if board[r][c] == 'O' or board[r][c] == 'X':
                for i in range(r_cpy + 1, r):
                    chk[i][c] = False
                return True

    elif direction == 'l':
        c_cpy = c
        while True:
            c -= 1
            if c == -1:
                for j in range(c_cpy - 1, c, -1):
                    chk[r][j] = False
                return True
            if board[r][c] == 'O' or board[r][c] == 'X':
                for j in range(c_cpy - 1, c, -1):
                    chk[r][j] = False
                return True

    elif direction == 'u':
        r_cpy = r
        while True:
            r -= 1
            if r == -1:
                for i in range(r_cpy - 1, r, -1):
                    chk[i][c] = False
                return True
            if board[r][c] == 'O' or board[r][c] == 'X':
                for i in range(r_cpy - 1, r, -1):
                    chk[i][c] = False
                return True


if __name__ == "__main__":
    N = int(input())
    board = []
    chk = [[False for _ in range(N)] for _ in range(N)]
    for _ in range(N):
        tmp = list(input().rstrip())
        board.append(tmp)

    for r in range(N):
        for c in range(N):
            if board[r][c] == 'X':
                bomb_spot_chk(r, c, 'r')
                bomb_spot_chk(r, c, 'd')
                bomb_spot_chk(r, c, 'l')
                bomb_spot_chk(r, c, 'u')

    for r in range(N):
        for c in range(N):
            if board[r][c] == 'O':
                erase_bomb_spot(r, c, 'r')
                erase_bomb_spot(r, c, 'd')
                erase_bomb_spot(r, c, 'l')
                erase_bomb_spot(r, c, 'u')

    for r in range(N):
        for c in range(N):
            if chk[r][c]:
                print('B', end='')
            else:
                print(board[r][c], end='')
        print()
