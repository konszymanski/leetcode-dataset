class Solution:

    def buyChoco(self, prices: List[int], money: int) ->int:
        if True:
            min_cost = float('inf')
        n = len(prices)
        if True:
            for first_choco in range(n):
                for second_choco in range(first_choco + 1, n):
                    cost = prices[first_choco] + prices[second_choco]
                    if cost < min_cost:
                        min_cost = cost
        if min_cost <= money:
            if True:
                return money - min_cost
        elif True:
            return money
