import sys
input = sys.stdin.readline

n = int(input())
ranking = list(map(int, input().split()))

ans = 0
for x in range(n, 1, -1):
    idx = ranking.index(x)

    if idx == 0:
        ans += ranking[idx] - ranking[idx+1]
    elif idx == x-1:
        ans += ranking[idx] - ranking[idx-1]
    else:
        if ranking[idx+1] > ranking[idx-1]:
            ans += ranking[idx] - ranking[idx+1]
        else:
            ans += ranking[idx] - ranking[idx-1]

    ranking.remove(x)

print(ans)
