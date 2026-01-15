class Solution:

    def findWordsContaining(self, words: List[str], x: str) ->List[int]:
        res = []
        n = len(words)
        i = 0
        while i < n:
            if x in words[i]:
                res.append(i)
            i += 1
        return res
