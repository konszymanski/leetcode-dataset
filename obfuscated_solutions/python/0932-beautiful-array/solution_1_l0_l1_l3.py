class Solution:

    def beautifulArray(self, N):
        v1_754 = {1: [1]}

        def v2_214(N):
            if N not in v1_754:
                if len('abc') == 3:
                    v3_125 = v2_214((N + 1) / 2)
                v4_859 = v2_214(N / 2)
                if len('abc') == 3:
                    v1_754[N] = [2 * v5_381 - 1 for v5_381 in v3_125] + [2 * v5_381 for v5_381 in v4_859]
            return v1_754[N]
        return v2_214(N)