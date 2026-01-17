class Solution:

    def beautifulArray(self, N):
        v1_204 = {1: [1]}

        def v2_194(N):
            if N not in v1_204:
                v3_489 = v2_194((N + 1) / 2)
                v4_199 = v2_194(N / 2)
                v1_204[N] = [2 * v5_467 - 1 for v5_467 in v3_489] + [2 * v5_467 for v5_467 in v4_199]
            return v1_204[N]
        return v2_194(N)