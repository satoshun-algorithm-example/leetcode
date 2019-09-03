#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
class Solution:
    def firstUniqChar(self, s: str) -> int:
        checked = []
        for i, c in enumerate(s):
            if c in checked:
                continue
            if s.count(c) == 1:
                return i
            checked.append(c)
        return -1
