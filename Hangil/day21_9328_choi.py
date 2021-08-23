import sys
from collections import deque

input = sys.stdin.readline

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)


def bfs():
    dq = deque()
    dq.append((0, 0))
    visit[0][0] = 1

    cnt = 0
    doors = [[] for x in range(26)]

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]

            if 0 <= x1 < h + 2 and 0 <= y1 < w + 2 and visit[x1][y1] == 0 and table[x1][y1] != '*':
                if table[x1][y1] == '$':
                    cnt += 1
                    visit[x1][y1] = 1
                    dq.append((x1, y1))

                elif 'A' <= table[x1][y1] <= 'Z':
                    door = ord(table[x1][y1]) - ord('A')
                    if keys[door]:
                        visit[x1][y1] = 1
                        dq.append((x1, y1))
                    else:
                        visit[x1][y1] = 1
                        doors[door].append((x1, y1))

                elif 'a' <= table[x1][y1] <= 'z':
                    visit[x1][y1] = 1
                    dq.append((x1, y1))
                    ky = ord(table[x1][y1]) - ord('a')
                    keys[ky] += 1
                    while doors[ky]:
                        tx, ty = doors[ky].pop()
                        dq.append((tx, ty))
                elif table[x1][y1] == '.':
                    visit[x1][y1] = 1
                    dq.append((x1, y1))

    return cnt


t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    table = [['.' for x in range(w + 2)]] + [['.'] + list(input().rstrip()) + ['.'] for x in range(h)] + [
        ['.' for x in range(w + 2)]]
    visit = [[0 for y in range(w + 2)] for x in range(h + 2)]

    keys = [0 for x in range(26)]

    kk = input().rstrip()
    if kk != '0':
        for k in kk:
            keys[ord(k) - ord('a')] = 1

    print(bfs())
