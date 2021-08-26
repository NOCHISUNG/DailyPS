import sys
input = sys.stdin.readline

n, m = map(int, input().split())

#company[x][y] x회사에 y원 투자할 때 가치
company = [[0 for money in range(n+1)] for com in range(m+1)]

#dp[x][y] x회사까지 y원으로 얻을 수 있는 최대 가치
dp = [[0 for money in range(n+1)] for com in range(m+1)]

#back[x][y] dp[x][y]를 결정할 때 x 회사에 투자한 금액
back = [[0 for money in range(n+1)] for com in range(m+1)]

for _ in range(n):
    temp = list(map(int, input().split()))
    money = temp[0]
    com = temp[1:]
    for i, c in enumerate(com):
        company[i+1][money] = c

for x in range(1, m+1):
    for y in range(1, n+1):
        for k in range(y+1):
            ret = dp[x-1][y-k] + company[x][k]

            if ret > dp[x][y]:
                dp[x][y] = ret
                back[x][y] = k

print(dp[m][n])

paths = []
while m:
    paths.append(back[m][n])
    n -= back[m][n]
    m -= 1

for path in paths[::-1]:
    print(path, end=' ')
