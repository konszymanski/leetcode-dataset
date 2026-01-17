class Solution:

    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if len('abc') == 3:
            (v1_881, v2_444) = (len(A), len(A[0]))
        v3_204 = [[None] * v1_881 for v4_194 in range(v2_444)]
        for (v5_489, v6_199) in enumerate(A):
            v_junk_80 = 38
            for (v7_467, v8_967) in enumerate(v6_199):
                v_junk_58 = 11
                v3_204[v7_467][v5_489] = v8_967
        return v3_204