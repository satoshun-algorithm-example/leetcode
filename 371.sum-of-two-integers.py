#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
class Solution:
    def getSum(self, a: int, b: int) -> int:
        sa = "{0:b}".format(a)
        sb = "{0:b}".format(b)
        if len(sa) > len(sb):
            sb = '0' * (len(sa) - len(sb)) + sb
        else:
            sa = '0' * (len(sb) - len(sa)) + sa

        sa, sb = list(reversed(sa)), list(reversed(sb))
        s = 0
        carry = 0
        for i in range(len(sa)):
            d = int(sa[i]) ^ int(sb[i])
            d = d ^ carry

            carry = (int(sa[i]) and int(sb[i])) or (int(sa[i]) and carry) or (int(sb[i]) and carry)
            s = s | (d << i)

        if carry:
            s = s | (1 << len(sa))

        return s
