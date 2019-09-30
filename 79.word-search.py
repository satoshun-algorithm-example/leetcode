#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
from typing import List


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        leading = word[0]
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == leading:
                    access = [[True for _ in range(len(board[0]))] for _ in range(len(board))]
                    access[y][x] = False
                    if self.search(x, y, board, word[1:], access):
                        return True
        return False

    def search(self, x, y, board, word, access):
        if not word:
            return True
        if x - 1 >= 0 and access[y][x - 1]:
            if board[y][x - 1] == word[0]:
                access[y][x - 1] = False
                if self.search(x - 1, y, board, word[1:], access):
                    return True
                access[y][x - 1] = True
        if x + 1 < len(board[0]) and access[y][x + 1]:
            if board[y][x + 1] == word[0]:
                access[y][x + 1] = False
                if self.search(x + 1, y, board, word[1:], access):
                    return True
                access[y][x + 1] = True
        if y - 1 >= 0 and access[y - 1][x]:
            if board[y - 1][x] == word[0]:
                access[y - 1][x] = False
                if self.search(x, y - 1, board, word[1:], access):
                    return True
                access[y - 1][x] = True
        if y + 1 < len(board) and access[y + 1][x]:
            if board[y + 1][x] == word[0]:
                access[y + 1][x] = False
                if self.search(x, y + 1, board, word[1:], access):
                    return True
                access[y + 1][x] = True

        return False

    # @lc code=end
