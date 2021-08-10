import sys
from math import gcd
input = sys.stdin.readline

n = int(input())
st1 = input().split()
st2 = input().split()

st2 += st2

cnt = 0

pi=[0 for x in range(n)]
j=0
for i in range(1,n):
    while j > 0 and st1[i] != st1[j]:
        j = pi[j-1]
    if st1[i] == st1[j]:
        j += 1
        pi[i] = j

j=0
for i in range(2*n-1):
    while j > 0 and st2[i] != st1[j]:
        j = pi[j-1]
    if st2[i] == st1[j]:
        if j == n-1:
            cnt += 1
            j = pi[j]
        else:
            j+=1

g = gcd(n, cnt)
print(str(cnt//g),'/',str(n//g), sep = '')
