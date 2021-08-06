import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def go():
    left = []
    right = []

    mid = arr[0]
    answer = [mid]

    for i, n in enumerate(arr[1:], 1):
        if n > mid:
            heappush(right, n)
        else:
            heappush(left, -n)

        if i % 2 == 0:
            if len(right) > len(left):
                heappush(left, -mid)
                mid = heappop(right)
            elif len(right) < len(left):
                heappush(right, mid)
                mid = -heappop(left)
                
            answer.append(mid)

    print(len(answer))
    for i, ans in enumerate(answer):
        if i != 0 and (i+1) % 10 == 1:
            print()
        print(ans, end=' ')
    print()


t = int(input())
for _ in range(t):
    m = int(input())
    arr = []

    if m % 10 == 0:
        for x in range(m//10):
            arr.extend(list(map(int, input().split())))
    else:
        for x in range(m//10 + 1):
            arr.extend(list(map(int, input().split())))

    go()
