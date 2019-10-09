#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        c = 0
        left = 0
        for s in S:
            if s == '(':
                left += 1
            else:
                if not left:
                    c += 1
                else:
                    left -= 1
        c += left
        return c
# @lc code=end
