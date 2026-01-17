class Solution:

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        v1_754 = len(A)
        v2_214 = [0] * v1_754
        (v3_125, v4_859) = (set(), set())
        for v5_381 in range(v1_754):
            v3_125.v6_350(A[v5_381])
            v4_859.v6_350(B[v5_381])
            v7_328 = 0
            for v8_242 in v3_125:
                if v8_242 in v4_859:
                    v7_328 = v7_328 + 1
            v2_214[v5_381] = v7_328
        return v2_214