#
# @lc app=leetcode id=1079 lang=python3
#
# [1079] Letter Tile Possibilities
#

# @lc code=start
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        c = 0
        for i in range(len(tiles)):
            target = set()
            self.calculate("", tiles, target, i + 1)
            c += len(target)

        return c

    def calculate(self, current, remain, target, count):
        if not count:
            target.add(current)
            return

        for i in range(len(remain)):
            self.calculate(current + remain[i], remain[:i] + remain[i + 1:], target, count - 1)

# @lc code=end
