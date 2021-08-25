"""
input :
6
1 6 2 5 3 4

output :
9
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__=="__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    if N == 1:
        print(nums[0])
        exit()

    tot = 0
    while True:
        max_val = max(nums)
        ind_of_max_val = nums.index(max_val)

        if ind_of_max_val == 0:
            tot += max_val - nums[ind_of_max_val + 1]
        elif ind_of_max_val == len(nums) - 1:
            tot += max_val - nums[ind_of_max_val - 1]
        else:
            tot += max_val - max(nums[ind_of_max_val + 1], nums[ind_of_max_val - 1])
        del nums[ind_of_max_val]

        if len(nums) == 1:
            break

    print(tot)
