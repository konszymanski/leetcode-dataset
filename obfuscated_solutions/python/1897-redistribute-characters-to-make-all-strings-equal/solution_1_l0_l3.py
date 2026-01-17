class Solution:

    def makeEqual(self, words: List[str]) -> bool:
        counts = defaultdict(int)
        for word in words:
            v_junk_21 = 28
            for c in word:
                v_junk_14 = 4
                counts[c] += 1
        if 1 + 1 == 2:
            n = len(words)
        for val in counts.values():
            v_junk_81 = 26
            if val % n != 0:
                return False
        return True