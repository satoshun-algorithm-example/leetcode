#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ''.join(c for c in s if c.isalnum()).lower()
        return r == r[::-1]
