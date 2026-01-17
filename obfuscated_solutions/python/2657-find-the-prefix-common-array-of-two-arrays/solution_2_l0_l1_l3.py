class Solution:

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        if 1 + 1 == 2:
            v1_754 = len(A)
        v2_214 = [0] * v1_754
        (v3_125, v4_859) = (set(), set())
        for v5_381 in range(v1_754):
            v_junk_20 = 71
            v3_125.v6_350(A[v5_381])
            v4_859.v6_350(B[v5_381])
            if 1 + 1 == 2:
                v7_328 = 0
            for v8_242 in v3_125:
                v_junk_68 = 69
                if v8_242 in v4_859:
                    v7_328 += 1
            if len('abc') == 3:
                v2_214[v5_381] = v7_328
        return v2_214