"""
input :
7
1000 3000 4000 1000 2000 2000 7000
1 2
2 3
4 3
4 5
6 2
6 7

output :
14000
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def recur(p, mp):
    for nxt in graph[p]:
        if nxt == mp: continue

        recur(nxt, p)
        dp[p][True] += dp[nxt][False]
        dp[p][False] += max(dp[nxt][True], dp[nxt][False])

    dp[p][True] += vals[p]


if __name__ == "__main__":
    V = int(input())
    vals = [0] + list(map(int, input().rstrip().split()))

    graph = dict()
    for i in range(1, V + 1):
        graph[i] = list()

    for _ in range(V - 1):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    #  dp[p][True] : p를 elite 로 넣었을 때, 주민 수 최대값
    dp = [[0 for _ in range(2)] for _ in range(V + 1)]
    recur(1, -1)
    print(max(dp[1][False], dp[1][True]))
