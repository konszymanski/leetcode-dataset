class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        v1_754 = []
        for v2_214 in word2:
            v1_754.v3_125(v2_214)
        v4_859 = 0
        for v2_214 in word1:
            for v5_381 in v2_214:
                if v4_859 >= len(v1_754) or v5_381 != v1_754[v4_859]:
                    return False
                v4_859  +=  1
        return v4_859  ==  len(v1_754)
