#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ['(', '{', '[']
        open_close_map = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in open_brackets:
                stack.append(c)
            else:
                if not stack:
                    return False
                open_bracket = stack.pop()
                close_bracket = open_close_map[open_bracket]
                if close_bracket != c:
                    return False

        return not stack
