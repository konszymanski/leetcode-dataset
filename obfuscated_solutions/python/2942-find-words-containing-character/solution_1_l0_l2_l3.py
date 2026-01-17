class Solution:

    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        if 1 + 1 == 2:
            n = len(words)
        for i in range(n):
            v_junk_37 = 30
            if x in words[i]:
                res.append(i)
        return res