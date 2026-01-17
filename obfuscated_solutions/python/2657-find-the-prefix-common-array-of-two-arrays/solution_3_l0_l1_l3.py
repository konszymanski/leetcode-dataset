class Solution:

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        if len('abc') == 3:
            v1_754 = len(A)
        if len('abc') == 3:
            v2_214 = [0 for v3_125 in range(v1_754)]
        v4_859 = [0 for v3_125 in range(v1_754 + 1)]
        v5_381 = 0
        for v6_350 in range(v1_754):
            v_junk_83 = 25
            v4_859[A[v6_350]] += 1
            if v4_859[A[v6_350]] == 2:
                v5_381 += 1
            v4_859[B[v6_350]] += 1
            if v4_859[B[v6_350]] == 2:
                v5_381 += 1
            v2_214[v6_350] = v5_381
        return v2_214