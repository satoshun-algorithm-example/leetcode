#
# @lc app=leetcode id=5232 lang=python3
#
# [5232]
#


# @lc code=start
class Solution:
    def balancedString(self, s: str) -> int:
        q = s.count("Q")
        w = s.count("W")
        e = s.count("E")
        r = s.count("R")

        c = 0
        while True:
            if q == w == e == r:
                return c

            c += 1
            ma = max(q, w, e, r)
            mi = min(q, w, e, r)
            if ma == q:
                q -= 1
                if mi == w:
                    w += 1
                elif mi == e:
                    e += 1
                else:
                    r += 1
            elif ma == w:
                w -= 1
                if mi == q:
                    q += 1
                elif mi == e:
                    e += 1
                else:
                    r += 1
            elif ma == e:
                e -= 1
                if mi == q:
                    q += 1
                elif mi == w:
                    w += 1
                else:
                    r += 1
            elif ma == r:
                r -= 1
                if mi == q:
                    q += 1
                elif mi == w:
                    w += 1
                else:
                    e += 1

# @lc code=end
