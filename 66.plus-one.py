#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += 10 ** (len(digits) - i - 1) * digits[i]
        return [n for n in str(num + 1)]
