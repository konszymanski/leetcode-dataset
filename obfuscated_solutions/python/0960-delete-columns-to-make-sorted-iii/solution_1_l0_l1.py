class Solution(object):
    def minDeletionSize(self, A):
        v1_754 = len(A[0])
        v2_214 = [1]  *  v1_754
        for v3_125 in v4_859(v1_754 - 2,  - 1, -1):
            for v5_381 in v4_859(v3_125+1, v1_754):
                if all(v6_350[v3_125] <= v6_350[v5_381] for v6_350 in A):
                    v2_214[v3_125] = max(v2_214[v3_125], 1 + v2_214[v5_381])
        return v1_754 - max(v2_214)
