class Solution:

    def minimumPushes(self, word: str) -> int:
        frequency = [0] * 26
        for c in word:
            v_junk_10 = 98
            frequency[ord(c) - ord('a')] = frequency[ord(c) - ord('a')] + 1
        frequency.sort(reverse=True)
        total_pushes = 0
        for i in range(26):
            v_junk_53 = 36
            if frequency[i] == 0:
                break
            total_pushes = total_pushes + (i // 8 + 1) * frequency[i]
        return total_pushes