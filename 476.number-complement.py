#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        s = ""
        for c in "{0:b}".format(num):
            if c == '0':
                s += '1'
            else:
                s += '0'

        return int(s, 2)
# @lc code=end
