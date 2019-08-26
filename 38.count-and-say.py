#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            x = 0
            l = len(s)
            tmp = ''
            while l > x:
                c = s[x]
                x += 1
                count = 1

                while len(s) > x and c == s[x]:
                    count += 1
                    x += 1

                tmp += '{}{}'.format(count, c)
            s = tmp

        return s
