#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        for size in range(len(s)):
            for i in range(len(s) - size):
                if i - 1 < 0:
                    r = s[i + size::-1]
                else:
                    r = s[i + size:i - 1:-1]

                if s[i:i + size + 1] == r:
                    c += 1

        return c
