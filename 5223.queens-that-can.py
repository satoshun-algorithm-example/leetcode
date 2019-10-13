#
# @lc app=leetcode id=701 lang=python3
#
# [5223]
#

# @lc code=start

from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        attacks = []

        def right():
            for x in range(king[1] + 1, 8):
                position = [king[0], x]
                for queen in queens:
                    if queen == position:
                        attacks.append(queen)
                        return

        def right_down():
            i = 0
            for x in range(king[1] + 1, 8):
                i += 1
                position = [king[0] + i, x]
                for queen in queens:
                    if queen == position:
                        attacks.append(queen)
                        return

        def down():
            for y in range(king[0] + 1, 8):
                position = [y, king[1]]
                for queen in queens:
                    if queen == position:
                        attacks.append(queen)
                        return

        def down_left():
            i = 0
            for y in range(king[0] + 1, 8):
                i += 1
                position = [y, king[1] - 1]
                for queen in queens:
                    if queen == position:
                        attacks.append(queen)
                        return

        def left():
            for x in range(king[1] - 1, -1, -1):
                position = [king[0], x]
                for queen in queens:
                    if queen == position:
                        attacks.append(queen)
                        return

        def left_top():
            i = 0
            for x in range(king[1] - 1, -1, -1):
                i += 1
                position = [king[0] - i, x]
                for queen in queens:
                    if queen == position:
                        attacks.append(queen)
                        return

        def top():
            for y in range(king[0] - 1, -1, -1):
                position = [y, king[1]]
                for queen in queens:
                    if queen == position:
                        attacks.append(queen)
                        return

        def top_right():
            i = 0
            for y in range(king[0] - 1, -1, -1):
                i += 1
                position = [y, king[1] + i]
                for queen in queens:
                    if queen == position:
                        attacks.append(queen)
                        return

        right()
        right_down()
        down()
        down_left()
        left()
        left_top()
        top()
        top_right()

        return attacks

# @lc code=end
