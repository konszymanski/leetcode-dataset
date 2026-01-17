class Solution:

    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        (v1_754, v2_214) = (len(A), len(A[0]))
        v3_125 = [[None] * v1_754 for v4_859 in range(v2_214)]
        for (v5_381, v6_350) in enumerate(A):
            for (v7_328, v8_242) in enumerate(v6_350):
                v3_125[v7_328][v5_381] = v8_242
        return v3_125