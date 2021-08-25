import sys
input = sys.stdin.readline

n, k = map(int, input().split())

#table[x][y] x가 y보다 앞
table = [[False for y in range(n+1)] for x in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    table[a][b] = True

for t in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            if table[x][t] and table[t][y]:
                table[x][y] = True

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())

    if table[a][b]:
        print(-1)
    elif table[b][a]:
        print(1)
    else:
        print(0)