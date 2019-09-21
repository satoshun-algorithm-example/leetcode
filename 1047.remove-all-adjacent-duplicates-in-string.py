#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#
class Solution:
    def removeDuplicates(self, S: str) -> str:
        while True:
            find = False
            for (c1, c2) in zip(S[:len(S)], S[1:]):
                if c1 == c2:
                    find = True
                    S = S.replace(c1 + c2, "", 1)
                    break

            if not find:
                break

        return S
