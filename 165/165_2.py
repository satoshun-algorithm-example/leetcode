from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        jumbo = (tomatoSlices - (2 * cheeseSlices)) / 2
        if jumbo < 0:
            return []
        if int(jumbo) != jumbo:
            return []

        jumbo = int(jumbo)

        small = cheeseSlices - jumbo
        if small < 0:
            return []

        return [jumbo, small]
