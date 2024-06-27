class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)

        i, j = 0, 0
        maxV = 0
        count = 0

        while j < n:
            if s[j] in {'a', 'e', 'i', 'o', 'u'}:
                count += 1

            if (j - i + 1) == k:
                maxV = max(maxV, count)
                if s[i] in {'a', 'e', 'i', 'o', 'u'}:
                    count -= 1
                i += 1
            j += 1

        return maxV
