#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = 0
        for c in set(s):
            count = s.count(c)
            rest = count % 2
            if rest != 0:
                odd += 1
        return len(s) - odd + 1 if odd else len(s)
