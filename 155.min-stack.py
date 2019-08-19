#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        m = self.getMin()
        if m is None or m > x:
            m = x
        self.data.append((x, m))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        if len(self.data) == 0:
            return None
        return self.data[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
