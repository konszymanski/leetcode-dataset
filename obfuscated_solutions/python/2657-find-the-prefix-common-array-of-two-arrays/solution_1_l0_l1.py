class Solution:
    def findThePrefixCommonArray(self, A: list, B: list) -> list:
        v1_754 = len(A)
        v2_214 = [0]  *  v1_754
        for v3_125 in range(v1_754):
            v4_859 = 0
            for v5_381 in range(v3_125 + 1):
                for v6_350 in range(v3_125 + 1):
                    if A[v5_381]  ==  B[v6_350]:
                        v4_859  +=  1
                        break
            v2_214[v3_125] = v4_859
        return v2_214
