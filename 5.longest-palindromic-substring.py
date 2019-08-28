#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        r = s[0]
        ml = 1
        for i in range(1, len(s) - 1):
            cl = 0

            while True:
                left = i - cl
                right = i + cl
                if left < 0:
                    break
                if right >= len(s):
                    break
                if s[left] != s[right]:
                    break
                cl += 1

            cl -= 1
            if ml < (cl + 1) * 2 - 1:
                left = i - cl
                right = i + cl
                r = s[left:right + 1]
                ml = len(r)

        return r
