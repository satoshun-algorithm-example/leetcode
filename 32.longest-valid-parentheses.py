#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        i = 0
        l = len(s)
        m = 0
        while True:
            if l <= i:
                break

            if s[i] == ')':
                i += 1
                continue
            t, i = self.find(s, i)
            if t > m:
                m = t

        return m

    def find(self, s, index):
        i = 0
        m = 0
        while True:
            if i % 2 == 0:
                try:
                    if s[index + i] == '(':
                        m += 1
                        i += 1
                        continue
                except:
                    pass
                break
            else:
                try:
                    if s[index + i] == ')':
                        m += 1
                        i += 1
                        continue
                except:
                    pass
                m -= 1
                break

        return m, index + i

