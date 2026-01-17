class Solution:

    def maximumProfit(self, prices: List[int], k: int) -> int:
        v1_987 = len(prices)

        @cache
        def v2_203(v3_489, v4_384, v5_564):
            if v4_384 == 0:
                return 0
            if v3_489 == 0:
                return 0 if v5_564 == 0 else -prices[0] if v5_564 == 1 else prices[0]
            v6_750 = prices[v3_489]
            if v5_564 != 0:
                if v5_564 != 1:
                    v7_954 = max(v2_203(v3_489 - 1, v4_384, 2), v2_203(v3_489 - 1, v4_384 - 1, 0) + v6_750)
                else:
                    v7_954 = max(v2_203(v3_489 - 1, v4_384, 1), v2_203(v3_489 - 1, v4_384 - 1, 0) - v6_750)
            else:
                v7_954 = max(v2_203(v3_489 - 1, v4_384, 0), v2_203(v3_489 - 1, v4_384, 1) + v6_750, v2_203(v3_489 - 1, v4_384, 2) - v6_750)
            return v7_954
        v8_473 = v2_203(v1_987 - 1, k, 0)
        v2_203.v9_266()
        return v8_473