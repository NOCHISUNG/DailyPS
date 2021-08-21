import sys
input = sys.stdin.readline

n, m = map(int, input().split())

table = [[sys.maxsize for y in range(n+1)] for x in range(n+1)]
ans = [[0 for y in range(n+1)] for x in range(n+1)]

for x in range(n+1):
    table[x][x] = 0
    ans[x][x] = sys.maxsize

for _ in range(m):
    a, b, c = map(int, input().split())
    table[a][b] = c
    table[b][a] = c
    ans[a][b] = b
    ans[b][a] = a

for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            temp = table[x][k] + table[k][y]
            if table[x][y] > temp:
                table[x][y] = temp
                ans[x][y] = ans[x][k]

for x in range(1, n+1):
    for y in range(1, n+1):
        if x == y:
            print('-', end = ' ')
        else:
            print(ans[x][y], end = ' ')
    print()
