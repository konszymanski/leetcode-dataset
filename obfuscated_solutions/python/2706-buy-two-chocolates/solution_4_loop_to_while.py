class Solution:

    def buyChoco(self, prices: List[int], money: int) ->int:
        freq = [0] * 101
        for p in prices:
            freq[p] += 1
        minimum = 0
        second_minimum = 0
        price = 1
        while price < 101:
            if freq[price] > 1:
                minimum = price
                second_minimum = price
                break
            elif freq[price] == 1:
                minimum = price
                break
            price += 1
        if second_minimum == 0:
            price = minimum + 1
            while price < 101:
                if freq[price] > 0:
                    second_minimum = price
                    break
                price += 1
        min_cost = minimum + second_minimum
        if min_cost <= money:
            return money - min_cost
        return money
