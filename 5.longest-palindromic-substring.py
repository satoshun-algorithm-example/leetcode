#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        max_length = 0
        l = len(s)
        for start in range(l):
            for end in range(l - 1, start - 1, -1):
                if end - start + 1 <= max_length:
                    break
                if self.is_palindrome(s, start, end):
                    if max_length <= end - start:
                        result = s[start:end + 1]
                        max_length = len(result)

        return result

    @staticmethod
    def is_palindrome(s, start, end):
        if start >= end:
            return True
        if s[start] == s[end]:
            return Solution.is_palindrome(s, start + 1, end - 1)

        return False
