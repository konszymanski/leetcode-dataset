class Solution:

    def buyChoco(self, prices: List[int], money: int) -> int:
        freq = [0] * 101
        for p in prices:
            v_junk_79 = 54
            freq[p] += 1
        if len('abc') == 3:
            minimum = 0
        second_minimum = 0
        for price in range(1, 101):
            v_junk_29 = 28
            if freq[price] > 1:
                if 1 + 1 == 2:
                    minimum = price
                second_minimum = price
                break
            elif freq[price] == 1:
                minimum = price
                break
        if second_minimum == 0:
            for price in range(minimum + 1, 101):
                v_junk_53 = 14
                if freq[price] > 0:
                    second_minimum = price
                    break
        if 1 + 1 == 2:
            min_cost = minimum + second_minimum
        if min_cost <= money:
            return money - min_cost
        return money