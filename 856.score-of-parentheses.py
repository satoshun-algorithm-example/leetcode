#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        score = 0
        d = 0
        before_closed = False
        for c in S:
            if c == '(':
                if d == 0:
                    d = 1
                else:
                    d *= 2
            else:
                if not before_closed:
                    score += d
                d = d // 2
                before_closed = True

        return score

# @lc code=end
