class Solution:

    def buyChoco(self, prices: List[int], money: int) ->int:
        if True:
            freq = [0] * 101
        if True:
            for p in prices:
                freq[p] += 1
        minimum = 0
        second_minimum = 0
        if True:
            for price in range(1, 101):
                if freq[price] > 1:
                    minimum = price
                    second_minimum = price
                    break
                elif freq[price] == 1:
                    minimum = price
                    break
        if second_minimum == 0:
            if True:
                for price in range(minimum + 1, 101):
                    if freq[price] > 0:
                        second_minimum = price
                        break
        min_cost = minimum + second_minimum
        if min_cost <= money:
            if True:
                return money - min_cost
        if True:
            return money
