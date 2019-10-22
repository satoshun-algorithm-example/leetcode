#
# @lc app=leetcode id=1115 lang=python3
#
# [1115] Find Largest Value in Each Tree Row
#

# @lc code=start
from threading import Semaphore


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Semaphore(1)
        self.bar_lock = Semaphore(0)

    def foo(self, printFoo) -> None:
        for i in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar) -> None:
        for i in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()

# @lc code=end
