#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        l = len(s)
        for start, c in enumerate(s):
            for end in range(start, l):
                if self.is_palindrome(s, start, end):
                    if len(result) <= end - start:
                        result = s[start:end+1]

        return result

    @staticmethod
    def is_palindrome(s, start, end):
        if start >= end:
            return True
        if s[start] == s[end]:
            return Solution.is_palindrome(s, start + 1, end - 1)

        return False
