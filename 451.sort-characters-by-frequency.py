#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        count_map = {}
        for c in s:
            count_map[c] = count_map.get(c, 0) + 1

        return "".join(sorted(s, key=lambda x: (count_map[x], x), reverse=True))
# @lc code=end
