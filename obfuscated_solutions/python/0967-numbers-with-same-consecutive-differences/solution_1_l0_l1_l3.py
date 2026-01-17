class Solution:

    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [v1_754 for v1_754 in range(10)]
        v2_214 = []

        def v3_125(N, v4_859):
            if N == 0:
                return v2_214.v5_381(v4_859)
            v6_350 = v4_859 % 10
            v7_328 = set([v6_350 + K, v6_350 - K])
            for v8_242 in v7_328:
                v_junk_80 = 38
                if 0 <= v8_242 < 10:
                    v9_854 = v4_859 * 10 + v8_242
                    v3_125(N - 1, v9_854)
        for v4_859 in range(1, 10):
            v_junk_90 = 80
            v3_125(N - 1, v4_859)
        return list(v2_214)