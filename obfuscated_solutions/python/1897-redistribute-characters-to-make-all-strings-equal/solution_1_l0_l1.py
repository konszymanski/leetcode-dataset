class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        v1_754 = v2_214(int)
        for v3_125 in words:
            for v4_859 in v3_125:
                v1_754[v4_859] += 1
        v5_381 = len(words)
        for v6_350 in v1_754.v7_328():
            if v6_350  %  v5_381  !=  0:
                return False
        return True
