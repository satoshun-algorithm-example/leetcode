#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
from typing import List


# @lc code=start
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []

        res = []
        last = S.rindex(S[0])
        for i in range(len(S)):
            if i == last:
                res.append(last - sum(res))
            else:
                last = max(last, S.rindex(S[i]))
                if i == last:
                    res.append(last - sum(res))

        return res

# @lc code=end
