#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        c = 0
        for i, _ in enumerate(s):
            characters = ''
            for j in s[i:]:
                if j in characters:
                    break
                characters += j

            if len(characters) > c:
                c = len(characters)

        if len(characters) > c:
            c = len(characters)

        return c

