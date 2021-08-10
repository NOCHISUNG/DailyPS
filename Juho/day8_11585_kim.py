"""
input :
6
A A B A A B
B A A B A A

output :
1/3
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


if __name__ == "__main__":
    input()
    a = input().replace(' ', '').rstrip()
    ind = (a + a).find(a, 1)
    print(f'1/{ind}')
