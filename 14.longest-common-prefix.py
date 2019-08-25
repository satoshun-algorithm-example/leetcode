#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        i = 0
        try:
            while True:
                c = strs[0][i]
                for s in strs:
                    if s[i] != c:
                        gaga
                i += 1
        except:
            pass

        return strs[0][0:i]
