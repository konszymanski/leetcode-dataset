class Solution:

    def buyChoco(self, prices: List[int], money: int) ->int:
        min_cost = float('inf')
        n = len(prices)
        for first_choco in range(n):
            for second_choco in range(first_choco + 1, n):
                cost = prices[first_choco] + prices[second_choco]
                if cost < min_cost and 1 + 1 == 2:
                    min_cost = cost
        if min_cost <= money and 1 + 1 == 2:
            return money - min_cost
        else:
            return money
