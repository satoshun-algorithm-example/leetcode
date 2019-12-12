#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
from typing import List


# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        find_nodes = []
        result = None
        for edge in edges:
            if edge[0] in find_nodes and edge[1] in find_nodes:
                result = edge
                continue
            find_nodes.extend(edge)

        return result

# @lc code=end
