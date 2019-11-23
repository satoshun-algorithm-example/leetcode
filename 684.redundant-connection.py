#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
from builtins import enumerate
from typing import List


# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        index_map = {}
        indicies = {}
        for i, edge in enumerate(edges):
            indicies[edge[0]] = indicies.get(edge[0], 0) + 1
            indicies[edge[1]] = indicies.get(edge[1], 0) + 1

            index_map[edge[0]] = i
            index_map[edge[1]] = i

        # return last edge when all edges is even
        if all(v == 2 for v in indicies.values()):
            return edges[-1]

        def find_cycle(current, visited):
            for edge in edges:
                # find!!
                if edge[0] == current and visited[0] == edge[1] and len(visited) != 1:
                    return visited
                if edge[1] == current and visited[0] == edge[0] and len(visited) != 1:
                    return visited

                # search
                if edge[0] == current and edge[1] not in visited:
                    find_cycle(edge[1], visited + [edge[0]])
                if edge[1] == current and edge[0] not in visited:
                    find_cycle(edge[0], visited + [edge[1]])

        def find_edge(visisted):
            last_edge = -1
            for v in visisted:
                candidate = index_map[v]
                last_edge = max(last_edge, candidate)

            return edges[last_edge]

        # return last cycle edge
        # find odd and only once
        index = [key for key, value in indicies.items() if value == 3][0]
        for edge in edges:
            if edge[0] == index:
                result = find_cycle(edge[1], [edge[0]])
                if result:
                    return find_edge(result)
            if edge[1] == index:
                result = find_cycle(edge[0], [edge[1]])
                if result:
                    return find_edge(result)

# @lc code=end
