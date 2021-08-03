import sys
input = sys.stdin.readline


def back():
    

table = []
for _ in range(5):
    temp = []
    st = input().rstrip()
    for s in st:
        temp.append(s)
    table.append(temp)

arr = []
visit = [0 for x in range(13)]

for x in range(5):
    for y in range(9):
        if table[x][y] == 'x':
            arr.append(0)
            continue
        if table[x][y] != '.':
            n = ord(table[x][y]) - 64
            arr.append(n)
            visit[n] = 1

back()
