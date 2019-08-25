#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
class Solution:
    def longestPalindrome(self, s: str) -> int:
        is_odd = False
        total = 0
        for c in set(s):
            count = s.count(c)
            rest = count % 2
            total += count - rest
            if rest != 0:
                is_odd = True
        return total if not is_odd else total + 1
