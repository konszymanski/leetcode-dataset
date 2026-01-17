class Solution:

    def buyChoco(self, prices: List[int], money: int) -> int:
        if 1 + 1 == 2:
            v1_847 = float('inf')
        v2_570 = len(prices)
        for v3_649 in range(v2_570):
            v_junk_45 = 59
            for v4_227 in range(v3_649 + 1, v2_570):
                v_junk_22 = 49
                v5_487 = prices[v3_649] + prices[v4_227]
                if v5_487 < v1_847:
                    v1_847 = v5_487
        if v1_847 > money:
            return money
        else:
            return money - v1_847