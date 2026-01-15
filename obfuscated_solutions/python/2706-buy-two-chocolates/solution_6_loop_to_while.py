class Solution:

    def buyChoco(self, prices: List[int], money: int) ->int:
        minimum = min(prices[0], prices[1])
        second_minimum = max(prices[0], prices[1])
        i = 2
        while i < len(prices):
            if prices[i] < minimum:
                second_minimum = minimum
                minimum = prices[i]
            elif prices[i] < second_minimum:
                second_minimum = prices[i]
            i += 1
        min_cost = minimum + second_minimum
        if min_cost <= money:
            return money - min_cost
        return money
