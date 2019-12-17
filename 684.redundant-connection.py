#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
from typing import List


# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [0] * len(edges)

        def find(x):
            if parent[x] == 0:
                return x
            return find(parent[x])

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False

            parent[root_x] = root_y
            return True

        for edge in edges:
            if not union(edge[0] - 1, edge[1] - 1):
                return edge

# @lc code=end
