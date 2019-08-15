#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# [2,-8,8,6,-14,-12,11,-10,13,14,7,3,10,-13,3,-15,7,3,-11,-8,4,5,9,11,7,1,3,13,14,-13,3,-6,-6,-12,-15,-12,-9,3,-15,-11,-6,-1,0,11,2,-12,3,-6,6,0,-6,-12,-10,-12,6,5,-4,-5,-5,-4,-11,13,5,-2,-13,-3,-7,-15,8,-15,12,-13,0,-3,6,9,-8,-6,10,5,9,-11,0,7,-15,-8,-3,-4,-6,7,7,-2,-2,-11,3,0,-6,12,0,-13,4,-3,11,-11,1,2,13,8,4,9,-1,-2,5,14,12,5,13,-6,-13,-8,9,1,5,-8,-2,-6,-1]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        l = len(nums)

        for i in range(1, l - 1):
            left = 0
            right = l - 1

            if nums[i - 1] == nums[i]:
                left = i - 1

            if i >= 2 and nums[i - 2] == nums[i - 1] == nums[i]:
                continue

            while True:
                if i <= left:
                    break
                if i >= right:
                    break

                s = nums[left] + nums[i] + nums[right]

                if s < 0:
                    left += 1
                    while i > left and nums[left - 1] == nums[left]:
                        left += 1
                    continue

                if s > 0:
                    right -= 1
                    while i < right and nums[right] == nums[right + 1]:
                        right -= 1
                    continue

                result += [[nums[left], nums[i], nums[right]]]

                left += 1
                while i > left and nums[left - 1] == nums[left]:
                    left += 1

                right -= 1
                while i < right and nums[right] == nums[right + 1]:
                    right -= 1

        return result
