#
# @lc app=leetcode id=1079 lang=python3
#
# [1079] Letter Tile Possibilities
#

# @lc code=start
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        d = {}
        for tile in tiles:
            d[tile] = d.get(tile, 0) + 1

        def dfs():
            total = 0
            for key in d.keys():
                if not d[key]:
                    continue
                total += 1
                d[key] -= 1
                total += dfs()
                d[key] += 1
            return total

        return dfs()

# @lc code=end
