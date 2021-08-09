import sys
input = sys.stdin.readline


def check(m):
    hp = m
    atk = H_atk

    for t, a, h in rooms:
        if t == 1:
            if (h-1)//atk > (hp-1)//a:
                return False
            else:
                hp -= (h-1)//atk * a
        else:
            atk += a
            hp = min(hp + h, m)

    return True
    

n, H_atk = map(int, input().split())

rooms = [list(map(int, input().split())) for x in range(n)]

left = 1
right = 999999000001 * n

while left <= right:
    mid = (left + right)//2

    if check(mid):
        right = mid - 1
    else:
        left = mid + 1

print(left)
