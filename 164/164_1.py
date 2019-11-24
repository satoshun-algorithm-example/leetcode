from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        distance = 0
        for i in range(len(points) - 1):
            distance += max(
                abs(points[i][0] - points[i + 1][0]),
                abs(points[i][1] - points[i + 1][1]),
            )

        return distance
