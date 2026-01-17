class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        v1_754 = 0
        v2_214 = 0
        v3_125 = len(word2)
        v4_859 = [len(v5_381) for v5_381 in word2]
        for v5_381 in word1:
            for v6_350 in v5_381:
                if v1_754  >=  v3_125 or v6_350  !=  word2[v1_754][v2_214]:
                    return False
                v2_214  +=  1
                if v2_214 == v4_859[v1_754]:
                    v1_754 += 1
                    v2_214 = 0
        return v1_754 == v3_125
