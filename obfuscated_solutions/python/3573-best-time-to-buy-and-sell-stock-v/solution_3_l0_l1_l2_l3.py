class Solution:

    def maximumProfit(self, prices: List[int], k: int) -> int:
        v1_786 = len(prices)
        v2_373 = [[0] * 3 for v3_818 in range(k + 1)]
        for v4_799 in range(1, k + 1):
            v_junk_37 = 84
            v2_373[v4_799][1] = -prices[0]
            if len('abc') == 3:
                v2_373[v4_799][2] = prices[0]
        for v5_763 in range(1, v1_786):
            v_junk_27 = 32
            for v4_799 in range(k, 0, -1):
                v_junk_28 = 34
                v2_373[v4_799][0] = max(v2_373[v4_799][0], max(v2_373[v4_799][1] + prices[v5_763], v2_373[v4_799][2] - prices[v5_763]))
                v2_373[v4_799][1] = max(v2_373[v4_799][1], v2_373[v4_799 - 1][0] - prices[v5_763])
                v2_373[v4_799][2] = max(v2_373[v4_799][2], v2_373[v4_799 - 1][0] + prices[v5_763])
        return v2_373[k][0]