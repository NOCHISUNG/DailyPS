import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs(sz, sx, sy):
    dq = deque()
    dq.append((sz, sx, sy))
    visit = [[[-1 for z in range(c)] for y in range(r)] for x in range(l)]
    visit[sz][sx][sy] = 0

    while dq:
        z, x, y = dq.popleft()

        for i in range(6):
            x1 = x + dx[i]
            y1 = y + dy[i]
            z1 = z + dz[i]

            if 0 <= x1 < r and 0 <= y1 < c and 0 <= z1 < l:
                if table[z1][x1][y1] == 'E':
                    print('Escaped in', visit[z][x][y]+1,'minute(s).')
                    return

                if visit[z1][x1][y1] == -1 and table[z1][x1][y1] == '.':
                    visit[z1][x1][y1] = visit[z][x][y] + 1
                    dq.append((z1, x1, y1))

    print('Trapped!')
    return
        

while True:
    l, r, c = map(int, input().split())

    if l == r == c == 0:
        break

    table = [[[]*c for y in range(r)] for x in range(l)]

    for x in range(l):
        table[x] = [list(map(str, input().rstrip())) for i in range(r)]
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if table[i][j][k] == 'S':
                    bfs(i, j, k)
