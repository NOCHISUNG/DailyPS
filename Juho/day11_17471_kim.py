"""
input :
6
5 2 3 4 1 2
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2

output :
1
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = 10 ** 4


def gen_min_diff(ind):
    global ans
    if ind == N + 1:
        if is_connected():
            tot1 = 0
            tot2 = 0
            for i in range(1, N + 1):
                if is_Asect[i]: tot1 += people[i]
                else: tot2 += people[i]
            ans = min(ans, abs(tot1 - tot2))
        return

    is_Asect[ind] = True
    gen_min_diff(ind + 1)
    is_Asect[ind] = False
    gen_min_diff(ind + 1)


def is_connected():
    a_spot = -1
    b_spot = -1
    for i in range(1, N + 1):
        if is_Asect[i]:
            a_spot = i
        else:
            b_spot = i

    if a_spot == -1: return False
    if b_spot == -1: return False

    visited = [False for _ in range(N + 1)]
    que = deque()
    que.append(a_spot)
    visited[a_spot] = True
    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if visited[nxt]: continue
            if not is_Asect[nxt]: continue

            visited[nxt] = True
            que.append(nxt)

    que.append(b_spot)
    visited[b_spot] = True
    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if visited[nxt]: continue
            if is_Asect[nxt]: continue

            visited[nxt] = True
            que.append(nxt)

    for i in range(1, N + 1):
        if not visited[i]:
            return False

    return True


if __name__ == "__main__":
    N = int(input())
    people = ['_'] + list(map(int, input().rstrip().split()))

    graph = dict()
    for i in range(1, N + 1):
        graph[i] = list()

    for i in range(1, N + 1):
        line = list(map(int, input().rstrip().split()))
        graph[i] += line[1:]

    is_Asect = [False for _ in range(N + 1)]
    ans = INF
    gen_min_diff(1)

    if ans != INF:
        print(ans)
    else:
        print(-1)
