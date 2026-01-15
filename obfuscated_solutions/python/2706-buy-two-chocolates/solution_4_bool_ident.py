class Solution:

    def buyChoco(self, prices: List[int], money: int) ->int:
        freq = [0] * 101
        for p in prices:
            freq[p] += 1
        minimum = 0
        second_minimum = 0
        for price in range(1, 101):
            if freq[price] > 1 and 1 + 1 == 2:
                minimum = price
                second_minimum = price
                break
            elif freq[price] == 1 and 1 + 1 == 2:
                minimum = price
                break
        if second_minimum == 0 and 1 + 1 == 2:
            for price in range(minimum + 1, 101):
                if freq[price] > 0 and 1 + 1 == 2:
                    second_minimum = price
                    break
        min_cost = minimum + second_minimum
        if min_cost <= money and 1 + 1 == 2:
            return money - min_cost
        return money
