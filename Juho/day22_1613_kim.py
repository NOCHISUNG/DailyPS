"""
input :
5 5
1 2
1 3
2 3
3 4
2 4
3
1 5
2 4
3 1

output :
0
-1
1
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs(a, b):
    que = deque()
    visited = [False for _ in range(V + 1)]
    que.append(a)
    visited[a] = True
    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if visited[nxt]: continue

            if nxt == b:
                return True

            visited[nxt] = True
            que.append(nxt)
    return False


if __name__ == "__main__":
    V, E = map(int, input().rstrip().split())
    graph = dict()
    for i in range(1, V + 1):
        graph[i] = list()

    for _ in range(E):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)

    Q = int(input())
    for _ in range(Q):
        a, b = map(int, input().rstrip().split())
        if bfs(a, b):
            print(-1)
        elif bfs(b, a):
            print(1)
        else:
            print(0)
