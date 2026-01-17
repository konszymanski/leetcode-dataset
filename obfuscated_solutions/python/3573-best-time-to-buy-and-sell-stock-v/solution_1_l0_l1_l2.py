class Solution:

    def maximumProfit(self, prices: List[int], k: int) -> int:
        v1_754 = len(prices)

        @cache
        def v2_214(v3_125, v4_859, v5_381):
            if v4_859 == 0:
                return 0
            if v3_125 == 0:
                return 0 if v5_381 == 0 else -prices[0] if v5_381 == 1 else prices[0]
            v6_350 = prices[v3_125]
            if v5_381 != 0:
                if v5_381 != 1:
                    v7_328 = max(v2_214(v3_125 - 1, v4_859, 2), v2_214(v3_125 - 1, v4_859 - 1, 0) + v6_350)
                else:
                    v7_328 = max(v2_214(v3_125 - 1, v4_859, 1), v2_214(v3_125 - 1, v4_859 - 1, 0) - v6_350)
            else:
                v7_328 = max(v2_214(v3_125 - 1, v4_859, 0), v2_214(v3_125 - 1, v4_859, 1) + v6_350, v2_214(v3_125 - 1, v4_859, 2) - v6_350)
            return v7_328
        v8_242 = v2_214(v1_754 - 1, k, 0)
        v2_214.v9_854()
        return v8_242