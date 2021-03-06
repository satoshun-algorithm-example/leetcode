#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self._isMatch(s, p, 0, 0)

    def _isMatch(self, s: str, p: str, si: int, pi: int) -> bool:
        sl = len(s)
        pl = len(p)

        # finish each two
        if sl == si and pl == pi:
            return True

        # finish only one
        if sl <= si:
            return pl - 1 == pi and p[pl - 1] == '*'
        if pl <= pi:
            return False

        if p[pi] == '.':
            a = self._isMatch(s, p, si + 1, pi + 1)
            b = False
            if pl > pi + 1 and p[pi + 1] == '*':
                b = self._isMatch(s, p, si, pi + 2)
            return a or b

        if p[pi] == '*':
            if p[pi - 1] == '.' or s[si] == p[pi - 1]:
                return self._isMatch(s, p, si + 1, pi) or self._isMatch(s, p, si, pi + 1)
            return self._isMatch(s, p, si, pi + 1)

        if s[si] != p[pi] and (pl > pi + 1 and p[pi + 1] != '*'):
            return False

        a = self._isMatch(s, p, si + 1, pi + 1)
        b = False
        if pl > pi + 1 and p[pi + 1] == '*':
            b = self._isMatch(s, p, si, pi + 2)
        return a or b

