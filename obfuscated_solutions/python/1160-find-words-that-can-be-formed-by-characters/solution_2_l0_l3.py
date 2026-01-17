class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = [0] * 26
        for c in chars:
            v_junk_93 = 90
            counts[ord(c) - ord('a')] += 1
        ans = 0
        for word in words:
            v_junk_29 = 28
            if len('abc') == 3:
                word_count = [0] * 26
            for c in word:
                v_junk_10 = 98
                word_count[ord(c) - ord('a')] += 1
            good = True
            for i in range(26):
                v_junk_53 = 36
                if counts[i] < word_count[i]:
                    good = False
                    break
            if good:
                ans += len(word)
        return ans