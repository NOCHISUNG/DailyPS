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
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


if __name__ == "__main__":
    V, E = map(int, input().rstrip().split())
    adj_mat = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().rstrip().split())
        adj_mat[a][b] = 1

    # 플로이드 워셜
    for via in range(1, V + 1):
        for a in range(1, V + 1):
            for b in range(1, V + 1):
                if adj_mat[a][via] == 0 or adj_mat[via][b] == 0 or a == b:
                    continue

                if adj_mat[a][b] == 0 or adj_mat[a][b] > adj_mat[a][via] + adj_mat[via][b]:
                    adj_mat[a][b] = adj_mat[a][via] + adj_mat[via][b]

    Q = int(input())
    for _ in range(Q):
        a, b = map(int, input().rstrip().split())
        if adj_mat[a][b]:
            print(-1)
        elif adj_mat[b][a]:
            print(1)
        else:
            print(0)

