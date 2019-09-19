#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digits = sorted(digits)
        table = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        l = []

        def s(t, current):
            if not t:
                l.append(current)
                return

            v = table[int(t[0])]
            for c in v:
                s(t[1:], current + c)

        s(digits, '')

        return sorted(set(l))
