#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#
from typing import List


# @lc code=start
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zero_group = {}
        group = []
        for i, a in enumerate(A):
            if a == 0:
                group.append(i)
            else:
                if group:
                    zero_group[len(zero_group)] = group
                    group = []

        cache = []

        max_count = 0

        def dfs(remain, position, visited):
            nonlocal max_count

            if position < 0 or position >= len(zero_group):
                return
            if visited in cache:
                return
            if remain == 0:
                m = 0
                for a in A:
                    if a == 0:
                        max_count = max(m, max_count)
                        m = 0
                    else:
                        m += 1

            cache.append(visited)
            group = zero_group[position]

            # fill up and down
            if len(group) <= remain:
                for g in group:
                    A[g] = 1
                dfs(remain - len(group), position + 1, visited + [position])
                dfs(remain - len(group), position - 1, visited + [position])
                for g in group:
                    A[g] = 0
            else:
                for g in group[:remain]:
                    A[g] = 1
                m = 0
                for a in A:
                    if a == 0:
                        max_count = max(m, max_count)
                        m = 0
                    else:
                        m += 1
                for g in group[:remain]:
                    A[g] = 0

                for g in group[len(group) - remain:]:
                    A[g] = 1
                m = 0
                for a in A:
                    if a == 0:
                        max_count = max(m, max_count)
                        m = 0
                    else:
                        m += 1
                for g in group[len(group) - remain:]:
                    A[g] = 0

        for i in range(len(zero_group)):
            dfs(K, i, [])

        return max_count
# @lc code=end
