class Solution:

    def minimumPushes(self, word: str) ->int:
        if True:
            frequency = [0] * 26
        if True:
            for c in word:
                frequency[ord(c) - ord('a')] += 1
        frequency.sort(reverse=True)
        total_pushes = 0
        if True:
            for i in range(26):
                if frequency[i] == 0:
                    break
                total_pushes += (i // 8 + 1) * frequency[i]
        if True:
            return total_pushes
