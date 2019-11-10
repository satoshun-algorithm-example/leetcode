from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        res = [[0] * len(colsum) for _ in range(2)]
        for i, col in enumerate(colsum):
            if col == 0:
                continue
            if col == 2:
                upper -= 1
                lower -= 1
                res[0][i] = 1
                res[1][i] = 1
                continue

            if upper > lower:
                upper -= 1
                res[0][i] = 1
            else:
                lower -= 1
                res[1][i] = 1

        # no result
        if upper != 0 or lower != 0:
            return []

        return res
