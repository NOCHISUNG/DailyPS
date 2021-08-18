import sys
input = sys.stdin.readline

n = int(input())
B = list(map(int, input().split()))

A = []

for b in B:
    cnt = 0
    num = b

    while True:
        if num % 3 == 0:
            cnt += 1
            num //= 3
        else:
            break

    A.append((cnt, b))

A.sort(key=lambda x:(-x[0], x[1]))
for a in A:
    print(a[1], end= ' ')
