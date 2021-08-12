"""
input :
3
10010111
011000100110001
0110001011001

output :
NO
NO
YES
"""
import re
import sys
sys.stdin = open("input.txt", "r")


if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        text = sys.stdin.readline().rstrip()
        p = re.compile('(100+1+|01)+')
        m = p.fullmatch(text)

        if m:
            print("YES")
        else:
            print("NO")
