import sys
import re
input = sys.stdin.readline

pattern = '(100+1+|01)+'

t = int(input())
for _ in range(t):
    st = input().rstrip()
    p = re.compile(pattern)
    
    if p.fullmatch(st):
        print("YES")
    else:
        print("NO")
