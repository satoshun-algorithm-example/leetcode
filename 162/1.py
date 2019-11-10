from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat = [[0] * m for _ in range(n)]
        for i in indices:
            # row
            for j in range(m):
                mat[i[0]][j] += 1

            # column
            for j in range(n):
                mat[j][i[1]] += 1

        return sum(mat[y][x] % 2 for x in range(m) for y in range(n))
