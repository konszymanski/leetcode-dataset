class Solution:

    def buyChoco(self, prices: List[int], money: int) -> int:
        v1_754 = min(prices[0], prices[1])
        v2_214 = max(prices[0], prices[1])
        for v3_125 in range(2, len(prices)):
            if prices[v3_125] >= v1_754:
                if prices[v3_125] < v2_214:
                    v2_214 = prices[v3_125]
            else:
                v2_214 = v1_754
                v1_754 = prices[v3_125]
        v4_859 = v1_754 + v2_214
        if v4_859 <= money:
            return money - v4_859
        return money