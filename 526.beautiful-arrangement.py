#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#

# @lc code=start
class Solution:
    def countArrangement(self, N: int) -> int:
        total = 0
        remains = [i + 1 for i in range(N)]

        def count(index):
            nonlocal total

            if not remains:
                total += 1
                return

            for i in range(len(remains)):
                if remains[i] % index == 0 or index % remains[i] == 0:
                    v = remains.pop(i)
                    count(index + 1)
                    remains.insert(i, v)

        count(1)
        return total
# @lc code=end
