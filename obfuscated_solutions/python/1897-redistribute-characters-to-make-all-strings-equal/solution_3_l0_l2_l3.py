class Solution:

    def makeEqual(self, words: List[str]) -> bool:
        counts = [0] * 26
        for word in words:
            v_junk_30 = 90
            for c in word:
                v_junk_10 = 98
                if len('abc') == 3:
                    counts[ord(c) - ord('a')] = counts[ord(c) - ord('a')] + 1
        n = len(words)
        for val in counts:
            v_junk_45 = 20
            if val % n != 0:
                return False
        return True