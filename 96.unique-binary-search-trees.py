#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
class Solution:
    cache = {0: 1, 1: 1, 2: 2}

    def numTrees(self, n: int) -> int:
        return self.numTrees2(n=n)

    def numTrees2(self, n: int) -> int:
        if n in self.cache:
            return self.cache.get(n)

        s = 0
        for i in range(1, n + 1):
            s += (self.numTrees2(i - 1) * self.numTrees2(n - i))
        self.cache[n] = s
        return s
