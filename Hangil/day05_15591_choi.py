import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def bfs(start, k):
    dq = deque()
    dq.append((start, sys.maxsize))
    visit = [False for x in range(n+1)]
    visit[start] = True

    cnt = 0

    while dq:
        here, dist = dq.popleft()

        for there, cost in tree[here]:
            if visit[there]:
                continue

            temp = min(cost, dist)
            dq.append((there, temp))
            if temp >= k:
                cnt += 1
            visit[there] = True

    print(cnt)
    return


n, query = map(int, input().split())
tree = defaultdict(list)

for x in range(n-1):
    p, q, r = map(int, input().split())
    tree[p].append((q, r))
    tree[q].append((p, r))

for x in range(query):
    k, v = map(int, input().split())
    bfs(v, k)
