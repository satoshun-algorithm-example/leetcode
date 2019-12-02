from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for y in range(1, len(matrix)):
            for x in range(1, len(matrix[0])):
                matrix[y][x] *= (min(matrix[y - 1][x - 1], matrix[y - 1][x], matrix[y][x - 1]) + 1)

        return sum(map(sum, matrix))
