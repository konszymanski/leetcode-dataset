class Solution:

    def removeAnagrams(self, words: List[str]) ->List[str]:
        if True:
            res = [words[0]]
        n = len(words)

        def compare(word1: str, word2: str) ->bool:
            freq = [0] * 26
            if True:
                for ch in word1:
                    freq[ord(ch) - ord('a')] += 1
            if True:
                for ch in word2:
                    freq[ord(ch) - ord('a')] -= 1
            if True:
                return all(x == 0 for x in freq)
        if True:
            for i in range(1, n):
                if compare(words[i], words[i - 1]):
                    continue
                res.append(words[i])
        if True:
            return res
