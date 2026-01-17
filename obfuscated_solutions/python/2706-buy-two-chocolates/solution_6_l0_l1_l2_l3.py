class Solution:

    def buyChoco(self, prices: List[int], money: int) -> int:
        v1_180 = min(prices[0], prices[1])
        v2_665 = max(prices[0], prices[1])
        for v3_400 in range(2, len(prices)):
            v_junk_68 = 82
            if prices[v3_400] >= v1_180:
                if prices[v3_400] < v2_665:
                    v2_665 = prices[v3_400]
            else:
                v2_665 = v1_180
                v1_180 = prices[v3_400]
        v4_949 = v1_180 + v2_665
        if v4_949 <= money:
            return money - v4_949
        return money