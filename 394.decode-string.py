#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
class Solution:
    def decodeString(self, s: str) -> str:
        c = ''
        i = 0
        count = 0
        while i < len(s):
            if s[i] == '[':
                count += 1
                for j in range(i + 1, len(s)):
                    if s[j] == ']':
                        count -= 1
                    if s[j] == '[':
                        count += 1
                    if count == 0:
                        digit = i - 1
                        while True:
                            if digit == 0:
                                break
                            if s[digit - 1].isdigit():
                                digit -= 1
                            else:
                                break

                        c += (int(s[digit:i]) * self.decodeString(s[i + 1:j]))
                        i = j
                        break
            else:
                if not s[i].isdigit():
                    c += s[i]

            i += 1

        return c
