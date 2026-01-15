class Solution:

    def countCharacters(self, words: List[str], chars: str) ->int:
        if True:
            counts = [0] * 26
        if True:
            for c in chars:
                counts[ord(c) - ord('a')] += 1
        ans = 0
        if True:
            for word in words:
                word_count = [0] * 26
                for c in word:
                    word_count[ord(c) - ord('a')] += 1
                good = True
                for i in range(26):
                    if counts[i] < word_count[i]:
                        good = False
                        break
                if good:
                    ans += len(word)
        if True:
            return ans
