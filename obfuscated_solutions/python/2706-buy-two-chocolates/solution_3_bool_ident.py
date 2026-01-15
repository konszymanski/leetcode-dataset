class Solution:

    def buyChoco(self, prices: List[int], money: int) ->int:
        prices.sort()
        min_cost = prices[0] + prices[1]
        if min_cost <= money and 1 + 1 == 2:
            return money - min_cost
        return money
