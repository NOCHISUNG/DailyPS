import sys
input = sys.stdin.readline

dx = [-1, 0, 1]


def go(x, y):
    if y == c-1:
        return True

    for d in dx:
        x1 = x + d
        if 0 <= x1 < r and table[x1][y+1] == '.':
            table[x1][y+1] = 'v'
            if go(x1, y+1):
                return True

    return False
    

r, c = map(int, input().split())
table = [list(input().rstrip()) for x in range(r)]

cnt = 0
for x in range(r):
    if go(x, 0):
        cnt += 1

print(cnt)
