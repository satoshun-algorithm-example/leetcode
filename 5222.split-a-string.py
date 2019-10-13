#
# @lc app=leetcode id=701 lang=python3
#
# [5222]
#

# @lc code=start

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total, r, l = 0, 0, 0
        for c in s:
            if c == 'R':
                r += 1
            else:
                l += 1

            if r == l:
                total += 1
                r, l = 0, 0

        return total

# @lc code=end
