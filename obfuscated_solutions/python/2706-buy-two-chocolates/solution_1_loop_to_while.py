class Solution:

    def buyChoco(self, prices: List[int], money: int) ->int:
        min_cost = float('inf')
        n = len(prices)
        first_choco = 0
        while first_choco < n:
            for second_choco in range(first_choco + 1, n):
                cost = prices[first_choco] + prices[second_choco]
                if cost < min_cost:
                    min_cost = cost
            first_choco += 1
        if min_cost <= money:
            return money - min_cost
        else:
            return money
