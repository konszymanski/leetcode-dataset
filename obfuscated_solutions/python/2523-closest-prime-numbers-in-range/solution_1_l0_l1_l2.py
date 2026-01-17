class Solution:

    def _sieve(self, upper_limit):
        v1_754 = [True] * (upper_limit + 1)
        v1_754[0] = v1_754[1] = False
        for v2_214 in range(2, int(upper_limit ** 0.5) + 1):
            if v1_754[v2_214]:
                for v3_125 in range(v2_214 * v2_214, upper_limit + 1, v2_214):
                    v1_754[v3_125] = False
        return v1_754

    def v4_859(self, v5_381, v6_350):
        v7_328 = self._sieve(v6_350)
        v8_242 = [v9_854 for v9_854 in range(v5_381, v6_350 + 1) if v7_328[v9_854]]
        if len(v8_242) < 2:
            return (-1, -1)
        v10_204 = float('inf')
        v11_792 = (-1, -1)
        for v12_858 in range(1, len(v8_242)):
            v13_658 = v8_242[v12_858] - v8_242[v12_858 - 1]
            if v13_658 < v10_204:
                v10_204 = v13_658
                v11_792 = (v8_242[v12_858 - 1], v8_242[v12_858])
        return v11_792