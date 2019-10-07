#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#
from typing import List


# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = {0}
        if len(rooms) == 1:
            return True

        marks = [0]
        news = rooms[0]
        visit.update(rooms[0])
        while news:
            updated = []
            for n in news:
                if n not in marks:
                    visit.update(rooms[n])
                    updated.extend(rooms[n])
                    marks.append(n)
            news = updated
        return len(visit) == len(rooms)

# @lc code=end
