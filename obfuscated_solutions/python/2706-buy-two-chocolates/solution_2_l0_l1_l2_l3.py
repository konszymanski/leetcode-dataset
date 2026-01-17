class Solution:

    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.v1_132()
        v2_130 = prices[0] + prices[1]
        if v2_130 > money:
            return money
        else:
            return money - v2_130