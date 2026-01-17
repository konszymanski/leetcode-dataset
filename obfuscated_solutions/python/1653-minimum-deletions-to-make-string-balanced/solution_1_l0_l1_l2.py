class Solution:

    def minimumDeletions(self, s: str) -> int:
        v1_754 = len(s)
        v2_214 = [0] * v1_754
        v3_125 = [0] * v1_754
        v4_859 = 0
        for v5_381 in range(v1_754):
            v3_125[v5_381] = v4_859
            if s[v5_381] == 'b':
                v4_859 = v4_859 + 1
        v6_350 = 0
        for v5_381 in range(v1_754 - 1, -1, -1):
            v2_214[v5_381] = v6_350
            if s[v5_381] == 'a':
                v6_350 = v6_350 + 1
        v7_328 = v1_754
        for v5_381 in range(v1_754):
            v7_328 = min(v7_328, v2_214[v5_381] + v3_125[v5_381])
        return v7_328