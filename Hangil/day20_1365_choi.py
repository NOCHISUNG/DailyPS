import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []

for a in arr:
    if not stack or stack[-1] < a:
        stack.append(a)
    else:
        stack[bisect_left(stack, a)] = a

print(n - len(stack))
