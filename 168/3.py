class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = 0
        for end in range(minSize, len(s) + 1):
            c = 1
            target = s[end - minSize:end]
            if len(set(target)) > maxLetters:
                continue

            i = end - minSize
            while i - minSize >= 0:
                if s[i - minSize: i] == target:
                    c += 1
                    i -= minSize
                else:
                    i -= 1

            count = max(count, c)

        return count
