#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        r = ""
        for i in range(len(s)):
            t = self.substring(i, i, s)
            if len(r) < len(t):
                r = t
            t = self.substring(i, i + 1, s)
            if len(r) < len(t):
                r = t

        return r

    def substring(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
