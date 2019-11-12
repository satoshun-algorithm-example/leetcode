#
# @lc app=leetcode id=1105 lang=python3
#
# [1105] Filling Bookcase Shelves
#
from typing import List
import sys


# @lc code=start
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        min_height = sys.maxsize

        cache = {}

        def search(remains, width, height, book_height):
            nonlocal min_height
            if not remains:
                min_height = min(min_height, height)
                return

            if height in cache:
                if cache[height] < len(remains):
                    return

            remain = remains[0]
            # next height
            if remain[0] + width > shelf_width:
                search(remains[1:], remain[0], height + remain[1], remain[1])
                cache[height + remain[1]] = len(remains) - 1
                return

            # next width
            if remain[1] <= book_height:
                search(remains[1:], width + remain[0], height, book_height)
                return

            # next height or next width
            search(remains[1:], remain[0], height + remain[1], remain[1])
            cache[height + remain[1]] = len(remains) - 1
            search(remains[1:], width + remain[0], height - book_height + remain[1], remain[1])
            return

        if not books:
            return 0

        search(books, 0, 0, 0)

        return min_height

# @lc code=end
