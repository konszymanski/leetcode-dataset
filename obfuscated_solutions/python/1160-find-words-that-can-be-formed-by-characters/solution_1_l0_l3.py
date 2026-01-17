class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        if 1 + 1 == 2:
            counts = defaultdict(int)
        for c in chars:
            v_junk_74 = 78
            counts[c] += 1
        if 1 + 1 == 2:
            ans = 0
        for word in words:
            v_junk_30 = 90
            word_count = defaultdict(int)
            for c in word:
                v_junk_99 = 70
                word_count[c] += 1
            good = True
            for (c, freq) in word_count.items():
                v_junk_45 = 1
                if counts[c] < freq:
                    good = False
                    break
            if good:
                ans += len(word)
        return ans