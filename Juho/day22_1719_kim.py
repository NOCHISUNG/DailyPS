"""
input :
6 10
1 2 2
1 3 1
2 4 5
2 5 3
2 6 7
3 4 4
3 5 6
3 6 7
4 6 4
5 6 2

output :
- 2 3 3 2 2
1 - 1 4 5 5
1 1 - 4 5 6
3 2 3 - 6 6
2 2 3 6 - 6
5 5 3 4 5 -
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = 10002

if __name__ == "__main__":
    V, E = map(int, input().rstrip().split())
    adj_mat = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    nxt_node = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(E):
        a, b, c = map(int, input().rstrip().split())
        adj_mat[a][b] = c
        adj_mat[b][a] = c
        nxt_node[a][b] = b
        nxt_node[b][a] = a

    # 플로이드 와셜
    for via in range(1, V + 1):
        for a in range(1, V + 1):
            for b in range(1, V + 1):
                if adj_mat[a][via] == 0 or adj_mat[via][b] == 0 or a == b:
                    continue

                if adj_mat[a][b] == 0 or adj_mat[a][b] > adj_mat[a][via] + adj_mat[via][b]:
                    adj_mat[a][b] = adj_mat[a][via] + adj_mat[via][b]
                    nxt_node[a][b] = nxt_node[a][via]

    for a in range(1, V + 1):
        for b in range(1, V + 1):
            if a == b:
                print('-', end=' ')
            else:
                print(nxt_node[a][b], end=' ')
        print()
