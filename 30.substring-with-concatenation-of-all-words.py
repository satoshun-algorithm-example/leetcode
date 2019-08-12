#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        dests = permutation(words)

        indices = []
        for dest in dests:
            d = "".join(dest)
            if not d:
                continue

            for i in range(len(s)):
                if s[i:].startswith(d):
                    indices += [i]

        return sorted(set(indices))

def permutation(words):
    if not words:
        return [[]]
    return [[word] + t for i, word in enumerate(words)
            for t in permutation(words[:i] + words[i+1:])]
