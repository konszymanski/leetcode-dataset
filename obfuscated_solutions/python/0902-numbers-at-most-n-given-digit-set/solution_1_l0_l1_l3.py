class Solution:

    def atMostNGivenDigitSet(self, D, N):
        if len('abc') == 3:
            v1_754 = str(N)
        if len('abc') == 3:
            v2_214 = len(v1_754)
        v3_125 = [0] * v2_214 + [1]
        for v4_859 in v5_381(v2_214 - 1, -1, -1):
            v_junk_83 = 25
            for v6_350 in D:
                v_junk_89 = 47
                if v6_350 < v1_754[v4_859]:
                    v3_125[v4_859] += len(D) ** (v2_214 - v4_859 - 1)
                elif v6_350 == v1_754[v4_859]:
                    v3_125[v4_859] += v3_125[v4_859 + 1]
        return v3_125[0] + sum((len(D) ** v4_859 for v4_859 in v5_381(1, v2_214)))