"""
input :
3 4 5
S....
.###.
.##..
###.#

#####
#####
##.##
##...

#####
#####
#.###
####E

1 3 3
S##
#E#
###

0 0 0

output :
Escaped in 11 minute(s).
Trapped!
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs(s_node):
    que = deque()
    que.append(s_node)
    sz, sy, sx = s_node
    visited[sz][sy][sx] = 1

    while que:
        cz, cy, cx = que.popleft()
        for dz, dy, dx in move:
            nz, ny, nx = cz + dz, cy + dy, cx + dx
            if not (0 <= nz < L and 0 <= ny < R and 0 <= nx < C): continue
            if board[nz][ny][nx] == '#': continue
            if visited[nz][ny][nx]: continue

            visited[nz][ny][nx] = visited[cz][cy][cx] + 1
            if [nz, ny, nx] == e_node: break
            que.append([nz, ny, nx])

    ez, ey, ex = e_node
    return visited[ez][ey][ex]


if __name__ == "__main__":
    while True:
        L, R, C = map(int, input().rstrip().split())
        if [L, R, C] == [0, 0, 0]: break

        board = []
        for l in range(L):
            floor = []
            for r in range(R):
                line = list(input().rstrip())
                floor.append(line)
            board.append(floor)
            input()

        s_node = [-1, -1, -1]
        e_node = [-1, -1, -1]
        for l in range(L):
            for r in range(R):
                for c in range(C):
                    if board[l][r][c] == 'S':
                        s_node = [l, r, c]
                    elif board[l][r][c] == 'E':
                        e_node = [l, r, c]

        visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
        move = [[0, 0, 1], [0, 1, 0], [0, 0, -1], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]  # 동, 남, 서, 북, 상, 하
        res = bfs(s_node)
        if res != 0:
            print("Escaped in %d minute(s)." % (res - 1))
        else:
            print("Trapped!")
