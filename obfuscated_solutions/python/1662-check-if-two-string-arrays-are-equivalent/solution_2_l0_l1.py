class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        v1_754 = []
        v2_214 = []
        for v3_125 in word1:
            for v4_859 in v3_125:
                v1_754.v5_381(v4_859)
        for v3_125 in word2:
            for v4_859 in v3_125:
                v2_214.v5_381(v4_859)
        if len(v1_754)  !=  len(v2_214):
            return False
        for v6_350 in range(len(v1_754)):
            if v1_754[v6_350]  !=  v2_214[v6_350]:
                return False
        return True
