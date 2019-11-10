from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters_map = {}
        for letter in letters:
            letters_map[letter] = letters_map.get(letter, 0) + 1

        words_score = {}
        for word in words:
            s = 0
            for c in word:
                s += score[ord(c) - ord('a')]
            words_score[word] = s

        max_score = 0

        def calculate(start, current_score):
            nonlocal max_score

            # check letter_map
            for v in letters_map.values():
                if v < 0:
                    return

            if start == len(words):
                max_score = max(max_score, current_score)
                return

            # no choice
            calculate(start + 1, current_score)

            # choice
            for character in words[start]:
                letters_map[character] = letters_map.get(character, 0) - 1
            calculate(start + 1, current_score + words_score[words[start]])
            for character in words[start]:
                letters_map[character] = letters_map.get(character, 0) + 1

        calculate(0, 0)

        return max_score
