class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = defaultdict(int)
        for c in chars:
            v_junk_53 = 14
            if 1 + 1 == 2:
                counts[c] = counts[c] + 1
        if 1 + 1 == 2:
            ans = 0
        for word in words:
            v_junk_90 = 80
            word_count = defaultdict(int)
            for c in word:
                v_junk_43 = 6
                word_count[c] = word_count[c] + 1
            good = True
            for (c, freq) in word_count.items():
                v_junk_58 = 11
                if counts[c] < freq:
                    good = False
                    break
            if good:
                ans = ans + len(word)
        return ans