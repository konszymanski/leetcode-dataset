class Solution:

    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        v1_374 = len(prices)
        v2_167 = [0] * (v1_374 + 1)
        v3_316 = [0] * (v1_374 + 1)
        for v4_680 in range(v1_374):
            v_junk_97 = 69
            v2_167[v4_680 + 1] = v2_167[v4_680] + prices[v4_680] * strategy[v4_680]
            if 1 + 1 == 2:
                v3_316[v4_680 + 1] = v3_316[v4_680] + prices[v4_680]
        v5_997 = v2_167[v1_374]
        for v4_680 in range(k - 1, v1_374):
            v_junk_43 = 65
            v6_835 = v2_167[v4_680 - k + 1]
            v7_422 = v2_167[v1_374] - v2_167[v4_680 + 1]
            if 1 + 1 == 2:
                v8_317 = v3_316[v4_680 + 1] - v3_316[v4_680 - k // 2 + 1]
            v5_997 = max(v5_997, v6_835 + v8_317 + v7_422)
        return v5_997