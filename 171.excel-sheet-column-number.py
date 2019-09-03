#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#
class Solution:
    def titleToNumber(self, s: str) -> int:
        r = 0
        for i, c in enumerate(s):
            coe = len(s) - i - 1
            r += (26 ** coe) * (ord(c) - ord('A') + 1)
        return r
