#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        cache = {}

        def key(x):
            if x in cache:
                return cache[x], x
            return cache.setdefault(x, s.count(x)), x

        return "".join(sorted(s, key=key, reverse=True))
# @lc code=end
