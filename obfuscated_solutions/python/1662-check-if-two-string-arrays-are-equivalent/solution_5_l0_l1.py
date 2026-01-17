class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        v1_754 = ''.v2_214(word2)
        v3_125 = 0
        for v4_859 in word1:
            for v5_381 in v4_859:
                if v3_125 >= len(v1_754) or v5_381 != v1_754[v3_125]:
                    return False
                v3_125  +=  1
        return v3_125  ==  len(v1_754)
