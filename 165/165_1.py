from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # create board
        # -1 empty, 0 A, 1 B
        board = [[-1] * 3 for _ in range(3)]
        for i in range(len(moves)):
            move = moves[i]
            board[move[1]][move[0]] = i % 2

        def victory(value):
            if value == 0:
                return 'A'
            elif value == 1:
                return 'B'
            else:
                return 'Pending'

        for row in range(3):
            same = True
            i = board[row][0]
            for column in range(3):
                same = same and i == board[row][column]
            if same:
                return victory(i)
        for column in range(3):
            same = True
            i = board[0][column]
            for row in range(3):
                same = same and i == board[row][column]
            if same:
                return victory(i)

        if board[0][0] == board[1][1] == board[2][2]:
            return victory(board[1][1])

        if board[2][0] == board[1][1] == board[0][2]:
            return victory(board[1][1])

        if len(moves) == 9:
            return 'Draw'

        return 'Pending'
