#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        l = len(nums)
        for x in range(l):
            for y in range(x + 1, l):
                for z in range(y + 1, l):
                    if x == y:
                        break
                    if x == z:
                        continue
                    if y == z:
                        continue
                    if nums[x] + nums[y] + nums[z] == 0:
                        a = sorted([nums[x], nums[y], nums[z]])
                        if a not in result:
                            result += [a]

        return sorted(result)