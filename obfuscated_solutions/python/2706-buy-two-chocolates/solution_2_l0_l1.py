class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.v1_754()
        v2_214 = prices[0] + prices[1]
        if v2_214 <= money:
            return money  -  v2_214
        else:
            return money
