#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        i, ni, hl, nl = 0, 0, len(haystack), len(needle)
        while i < hl:
            c = haystack[i]

            if c == needle[ni]:
                ni += 1
                if ni >= nl:
                    return i - nl + 1
            else:
                i -= ni
                ni = 0

            i += 1

        return -1
