#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        a = [0]

        while len(a) < num + 1:
            a.extend(i + 1 for i in a[:])

        return a[:num + 1]
