import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(here):
    dp[here][0] = people[here-1]
    
    for there in tree[here]:
        if visit[there] == 0:
            visit[there] = 1
            dfs(there)

            dp[here][0] += dp[there][1]
            dp[here][1] += max(dp[there][0], dp[there][1])
            

n = int(input())
people = list(map(int, input().split()))
tree = [[] for x in range(n+1)]

#dp[x][y] x번째가 0 -> 포함, 1 -> X 일때 최대값
dp = [[0, 0] for x in range(n+1)]

visit = [0 for x in range(n+1)]

for x in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visit[1] = 1
dfs(1)

print(max(dp[1][0], dp[1][1]))
