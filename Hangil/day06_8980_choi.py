import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())

boxes = [list(map(int, input().split())) for x in range(m)]
boxes.sort(key=lambda x:x[1])

ans = 0
truck = [c for x in range(n+1)]

for x in range(m):
    temp = c
    for y in range(boxes[x][0], boxes[x][1]):
        temp = min(temp, truck[y])

    temp = min(temp, boxes[x][2])

    for y in range(boxes[x][0], boxes[x][1]):
        truck[y] -= temp

    ans += temp

print(ans)
