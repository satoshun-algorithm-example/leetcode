#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        in_dict = {}
        out_dict = {}
        for t in T:
            if t in S:
                in_dict[t] = in_dict.get(t, 0) + 1
            else:
                out_dict[t] = out_dict.get(t, 0) + 1

        res = ""
        for s in S:
            res += s * in_dict.get(s, 0)

        for k, v in out_dict.items():
            res += k * v

        return res

# @lc code=end
