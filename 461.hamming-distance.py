#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        return "{:b}".format(z).count('1')

# @lc code=end
