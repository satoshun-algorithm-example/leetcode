#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(sorted(s, key=lambda x: (s.count(x), x), reverse=True))
# @lc code=end
