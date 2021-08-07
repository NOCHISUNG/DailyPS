"""
input :
4 3
1 2 3
2 3 2
2 4 4
1 2
4 1
3 1

output :
3
0
2
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = 1000000005


def bfs(s_node):
    que = deque()
    que.append(s_node)
    visited[s_node] = INF - 1  # visited 했다는 표식

    while que:
        cur = que.popleft()
        for cur2nxt, nxt in graph[cur]:
            if visited[nxt] != INF:
                continue

            visited[nxt] = min(visited[cur], cur2nxt)
            que.append(nxt)


if __name__ == "__main__":
    N, Q = map(int, input().rstrip().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b, w = map(int, input().rstrip().split())
        graph[a].append([w, b])
        graph[b].append([w, a])

    for _ in range(Q):
        k, node = map(int, input().rstrip().split())

        visited = [INF for _ in range(N + 1)]
        bfs(node)
        cnt = 0
        for ind, usado in enumerate(visited):
            if ind == 0: continue
            if ind == node: continue
            if usado >= k:
                cnt += 1
        print(cnt)
