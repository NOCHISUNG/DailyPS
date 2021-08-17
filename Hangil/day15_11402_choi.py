import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def bi(n, r, p):
    if nCr[n][r] != -1:
        return nCr[n][r]
    if r == 0 or r == n:
        nCr[n][r] = 1
        return 1

    nCr[n][r] = (bi(n - 1, r - 1, p) + bi(n - 1, r, p)) % p
    return nCr[n][r]


def change(n, p):
    ret = []
    while n:
        ret.append(n % p)
        n //= p

    return ret


def solve(n, k, p):
    ans = 1
    np = change(n, p)
    nk = change(k, p)
    npl = len(np)
    npk = len(nk)
    le = max(npl, npk)
    for x in range(le):
        if x < npl:
            nn = np[x]
        else:
            nn = 0

        if x < npk:
            kk = nk[x]
        else:
            kk = 0

        if nn < kk:
            return 0

        ans *= bi(nn, kk, p)
        ans %= p

    return ans


nCr = [[-1 for x in range(2001)] for y in range(2001)]
n, k, m = map(int, input().split())
print(solve(n, k, m))
