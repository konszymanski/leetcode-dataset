class Solution:

    def makeEqual(self, words: List[str]) -> bool:
        if 1 + 1 == 2:
            counts = [0] * 26
        for word in words:
            v_junk_74 = 78
            for c in word:
                v_junk_37 = 30
                counts[ord(c) - ord('a')] += 1
        if 1 + 1 == 2:
            n = len(words)
        for val in counts:
            v_junk_93 = 90
            if val % n != 0:
                return False
        return True