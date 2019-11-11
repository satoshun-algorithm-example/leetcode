#
# @lc app=leetcode id=1105 lang=python3
#
# [1105] Filling Bookcase Shelves
#
from typing import List


# @lc code=start
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        min_height = 10000

        def search(remains, width, height, book_height):
            nonlocal min_height
            if not remains:
                min_height = min(min_height, height)
                return

            remain = remains[0]
            # next height
            if remain[0] + width > shelf_width:
                search(remains[1:], remain[0], height + remain[1], remain[1])
                return

            # next width
            if remain[1] <= book_height:
                search(remains[1:], width + remain[0], height, book_height)
                return

            # next height or next width
            search(remains[1:], remain[0], height + remain[1], remain[1])
            search(remains[1:], width + remain[0], height - book_height + remain[1], remain[1])
            return

        if not books:
            return 0

        search(books, 0, 0, 0)

        return min_height

# @lc code=end
