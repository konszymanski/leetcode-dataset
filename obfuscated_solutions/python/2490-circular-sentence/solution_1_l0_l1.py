class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        v1_754 = sentence.v2_214(" ")
        v3_125 = len(v1_754)
        v4_859 = v1_754[v3_125 - 1][ - 1]
        for v5_381 in range(v3_125):
            if v1_754[v5_381][0] != v4_859:
                return False
            v4_859 = v1_754[v5_381][ - 1]
        return True
