import sys
input = sys.stdin.readline


def f(p):
    ret = 0
    for i, x in enumerate(xs):
        ret += abs(p * i - x)
    return ret


n = int(input())
xs = list(map(int, input().split()))

left = 0
right = xs[n - 1]
while right - left >= 3:
    p1 = (left * 2 + right) // 3
    p2 = (left + right * 2) // 3

    if f(p1) < f(p2):
        right = p2
    else:
        left = p1

ans = sys.maxsize
for x in range(left, right + 1):
    ans = min(ans, f(x))

print(ans)
