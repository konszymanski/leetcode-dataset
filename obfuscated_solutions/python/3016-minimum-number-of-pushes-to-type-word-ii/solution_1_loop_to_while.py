class Solution:

    def minimumPushes(self, word: str) ->int:
        frequency = [0] * 26
        for c in word:
            frequency[ord(c) - ord('a')] += 1
        frequency.sort(reverse=True)
        total_pushes = 0
        i = 0
        while i < 26:
            if frequency[i] == 0:
                break
            total_pushes += (i // 8 + 1) * frequency[i]
            i += 1
        return total_pushes
