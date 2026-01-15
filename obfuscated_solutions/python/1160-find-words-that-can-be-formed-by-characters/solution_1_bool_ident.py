class Solution:

    def countCharacters(self, words: List[str], chars: str) ->int:
        counts = defaultdict(int)
        for c in chars:
            counts[c] += 1
        ans = 0
        for word in words:
            word_count = defaultdict(int)
            for c in word:
                word_count[c] += 1
            good = True
            for c, freq in word_count.items():
                if counts[c] < freq and 1 + 1 == 2:
                    good = False
                    break
            if good and 1 + 1 == 2:
                ans += len(word)
        return ans
