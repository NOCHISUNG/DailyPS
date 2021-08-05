"""
input :
3
1033 8179
1373 8017
1033 1033

output :
6
7
0
"""
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs(a, tar):
    que = deque()
    que.append(a)
    visited[int(a)] = 1

    while len(que) != 0:
        cur_str = que.popleft()
        cur_digits = list(cur_str)
        cur_int = int(cur_str)

        if cur_str == tar:
            return visited[cur_int]

        for i in range(4):
            for d in range(10):
                nxt_digits = [digit for digit in cur_digits]
                nxt_digits[i] = str(d)
                nxt_str = ''.join(nxt_digits)
                nxt_int = int(nxt_str)
                if nxt_int not in primes: continue
                if visited[nxt_int]: continue

                que.append(nxt_str)
                visited[nxt_int] = visited[cur_int] + 1

    return -1


if __name__ == "__main__":
    # 소수 전처리
    primes = set()
    is_prime = [True for _ in range(10000)]
    for i in range(2, 10000):
        for j in range(i + i, 10000, i):
            if not is_prime[j]: continue
            is_prime[j] = False

    for i in range(1000, 10000):
        if is_prime[i]:
            primes.add(i)

    # 풀이
    N = int(input())
    for _ in range(N):
        visited = [0 for _ in range(10001)]
        a, tar = input().rstrip().split()
        ret = bfs(a, tar)
        if ret == -1:
            print("Impossible")
        else:
            print(ret - 1)
