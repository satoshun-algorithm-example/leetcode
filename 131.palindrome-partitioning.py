#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

from typing import List


# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = []
        self.palindrome(0, s, [], palindromes)
        return palindromes

    def palindrome(self, i, s, pali, palindromes):
        if i == len(s):
            palindromes.append(pali)
            return

        for j in range(i + 1, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                self.palindrome(j, s, pali + [s[i:j]], palindromes)

# @lc code=end
