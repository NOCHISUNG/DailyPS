import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def move(x, y, i):
    m = 0
    while table[x+dx[i]][y+dy[i]] != '#' and table[x][y] != 'O':
        x += dx[i]
        y += dy[i]
        m += 1
    return x, y, m
    

def bfs():
    dq = deque()
    dq.append((0, rx, ry, bx, by))
    visit[rx][ry][bx][by] = 1

    while dq:
        cnt, rx1, ry1, bx1, by1 = dq.popleft()
        for i in range(4):
            rx2, ry2, rm = move(rx1, ry1, i)
            bx2, by2, bm = move(bx1, by1, i)

            if table[bx2][by2] == 'O':
                continue
            if table[rx2][ry2] == 'O':
                print(cnt + 1)
                return
            if rx2 == bx2 and ry2 == by2:
                if rm > bm:
                    rx2 -= dx[i]
                    ry2 -= dy[i]
                else:
                    bx2 -= dx[i]
                    by2 -= dy[i]
            if visit[rx2][ry2][bx2][by2] == 0:
                visit[rx2][ry2][bx2][by2] = 1
                dq.append((cnt+1, rx2, ry2, bx2, by2))
    print(-1)
    return
        

n, m = map(int, input().split())
table = [list(input().rstrip()) for x in range(n)]
visit = [[[[0 for bx in range(m)] for by in range(n)] for rx in range(m)] for ry in range(n)]

for x in range(n):
    for y in range(m):
        if table[x][y] == 'R':
            rx = x
            ry = y
        if table[x][y] == 'B':
            bx = x
            by = y

bfs()
