class Solution:

    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        v1_754 = []
        v2_214 = len(words)
        for v3_125 in range(v2_214):
            if x in words[v3_125]:
                v1_754.v4_859(v3_125)
        return v1_754