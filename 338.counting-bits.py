#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        a = []

        for i in range(num + 1):
            a.append(bin(i).count('1'))

        return a
