#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cases = string.ascii_lowercase + string.digits
        r = ""
        for c in s:
            if c in cases:
                r += c

        return r == r[::-1]
