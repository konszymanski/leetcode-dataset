class Solution:

    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        if 1 + 1 == 2:
            res = []
        n = len(words)
        for i in range(n):
            v_junk_79 = 12
            if x in words[i]:
                res.append(i)
        return res