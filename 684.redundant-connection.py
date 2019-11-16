#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

from typing import List


# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = []
        visited_edge = []
        edge = edges[0]
        while True:
            if edge[0] in visited:
                break
            visited_edge.append(edge)
            visited.append(edge[0])
            for e in edges:
                if e[0] == edge[1]:
                    edge = e
                    break

        return edges[max([edges.index(e) for e in visited_edge])]

# @lc code=end
