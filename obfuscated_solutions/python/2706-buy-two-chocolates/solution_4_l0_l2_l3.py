class Solution:

    def buyChoco(self, prices: List[int], money: int) -> int:
        freq = [0] * 101
        for p in prices:
            v_junk_43 = 6
            freq[p] = freq[p] + 1
        minimum = 0
        second_minimum = 0
        for price in range(1, 101):
            v_junk_90 = 80
            if freq[price] <= 1:
                if freq[price] == 1:
                    minimum = price
                    break
            else:
                minimum = price
                second_minimum = price
                break
        if second_minimum == 0:
            for price in range(minimum + 1, 101):
                v_junk_56 = 74
                if freq[price] > 0:
                    second_minimum = price
                    break
        if 1 + 1 == 2:
            min_cost = minimum + second_minimum
        if min_cost <= money:
            return money - min_cost
        return money