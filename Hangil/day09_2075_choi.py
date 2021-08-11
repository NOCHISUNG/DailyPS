import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
heap = []

for x in range(n):
    table = list(map(int, input().split()))

    if x == 0:
        for t in table:
            heappush(heap, t)
        continue

    for t in table:
        if t > heap[0]:
            heappush(heap, t)
            heappop(heap)

print(heap[0])
    
