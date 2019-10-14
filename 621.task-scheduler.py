#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for c in tasks:
            count[ord(c) - ord('A')] += 1

        count.sort(reverse=True)

        i = 0
        while i < 26 and count[i] == count[0]:
            i += 1

        return max(
            len(tasks),
            (count[0] - 1) * (n + 1) + i
        )
