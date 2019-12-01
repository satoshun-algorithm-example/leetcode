from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        jumbo = 0
        small = 0

        while not (tomatoSlices == 0 and cheeseSlices == 0):
            if tomatoSlices == cheeseSlices * 2:
                small = cheeseSlices
                break

            tomatoSlices -= 4
            cheeseSlices -= 1
            jumbo += 1
            if cheeseSlices < 0 or tomatoSlices < 0:
                return []

        return [jumbo, small]
