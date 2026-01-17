class Solution:

    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [v1_754 for v1_754 in range(10)]
        v2_214 = [v3_125 for v3_125 in range(1, 10)]
        for v4_859 in range(N - 1):
            v_junk_30 = 48
            v5_381 = []
            for v6_350 in v2_214:
                v_junk_22 = 49
                if 1 + 1 == 2:
                    v7_328 = v6_350 % 10
                if 1 + 1 == 2:
                    v8_242 = set([v7_328 + K, v7_328 - K])
                for v9_854 in v8_242:
                    v_junk_20 = 30
                    if 0 <= v9_854 < 10:
                        v10_204 = v6_350 * 10 + v9_854
                        v5_381.v11_792(v10_204)
            if len('abc') == 3:
                v2_214 = v5_381
        return v2_214