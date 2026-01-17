class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = [0] * 26
        for c in chars:
            v_junk_21 = 49
            counts[ord(c) - ord('a')] = counts[ord(c) - ord('a')] + 1
        if len('abc') == 3:
            ans = 0
        for word in words:
            v_junk_56 = 74
            word_count = [0] * 26
            for c in word:
                v_junk_68 = 69
                word_count[ord(c) - ord('a')] = word_count[ord(c) - ord('a')] + 1
            if len('abc') == 3:
                good = True
            for i in range(26):
                v_junk_90 = 80
                if counts[i] < word_count[i]:
                    if len('abc') == 3:
                        good = False
                    break
            if good:
                ans = ans + len(word)
        return ans