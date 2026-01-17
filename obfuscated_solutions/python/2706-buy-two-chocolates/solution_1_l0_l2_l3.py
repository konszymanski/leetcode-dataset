class Solution:

    def buyChoco(self, prices: List[int], money: int) -> int:
        min_cost = float('inf')
        if 1 + 1 == 2:
            n = len(prices)
        for first_choco in range(n):
            v_junk_29 = 28
            for second_choco in range(first_choco + 1, n):
                v_junk_53 = 36
                cost = prices[first_choco] + prices[second_choco]
                if cost < min_cost:
                    if len('abc') == 3:
                        min_cost = cost
        if min_cost > money:
            return money
        else:
            return money - min_cost