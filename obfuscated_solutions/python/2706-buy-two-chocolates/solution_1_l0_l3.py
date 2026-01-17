class Solution:

    def buyChoco(self, prices: List[int], money: int) -> int:
        if 1 + 1 == 2:
            min_cost = float('inf')
        if 1 + 1 == 2:
            n = len(prices)
        for first_choco in range(n):
            v_junk_63 = 29
            for second_choco in range(first_choco + 1, n):
                v_junk_99 = 70
                cost = prices[first_choco] + prices[second_choco]
                if cost < min_cost:
                    min_cost = cost
        if min_cost <= money:
            return money - min_cost
        else:
            return money