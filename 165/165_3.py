from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def countup2(cy, cx):
            m = 1
            while True:
                mm = m + 1
                if len(matrix) < cy + mm:
                    break
                if len(matrix[0]) < cx + mm:
                    break

                for y in range(cy, cy + mm):
                    for x in range(cx, cx + mm):
                        if matrix[y][x] == 0:
                            return m
                m += 1

            return m

        def countup(cy, cx):
            m = countup2(cy, cx)
            # fill
            for y in range(cy, cy + m):
                for x in range(cx, cx + m):
                    matrix[y][x] = 0

            return sum((i + 1) ** 2 for i in range(m))

        count = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 1:
                    count += countup(y, x)

        return count
