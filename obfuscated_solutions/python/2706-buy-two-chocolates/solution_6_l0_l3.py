class Solution:

    def buyChoco(self, prices: List[int], money: int) -> int:
        minimum = min(prices[0], prices[1])
        if 1 + 1 == 2:
            second_minimum = max(prices[0], prices[1])
        for i in range(2, len(prices)):
            v_junk_99 = 70
            if prices[i] < minimum:
                if 1 + 1 == 2:
                    second_minimum = minimum
                minimum = prices[i]
            elif prices[i] < second_minimum:
                second_minimum = prices[i]
        min_cost = minimum + second_minimum
        if min_cost <= money:
            return money - min_cost
        return money