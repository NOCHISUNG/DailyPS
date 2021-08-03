import sys
from collections import deque
input = sys.stdin.readline


def isPrime(n):
    for x in range(2, int(n ** 0.5)+1):
        if n%x == 0:
            return False
    return True


def go(start, end):
    visit = dict(zip(primes, [0 for x in range(len(primes))]))
    visit[start] = 1
    dq = deque()
    dq.append((start, 0))

    while dq:
        n, cnt = dq.popleft()

        if n == end:
            return print(cnt)
        
        temp = list(str(n))

        for x in range(4):
            for y in range(10):
                new_temp = temp[:]
                new_temp[x] = str(y)
                nxt = int(''.join(new_temp))
                if nxt in primes and visit[nxt] == 0:
                    visit[nxt] = 1
                    dq.append((nxt, cnt+1))

    return print('Impossible')
    

primes = []
for p in range(1001, 10000):
    if isPrime(p):
        primes.append(p)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    go(a, b)
