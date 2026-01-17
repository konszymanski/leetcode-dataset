class Solution:

    def indexMinimum(self, arr: List[int]) -> int:
        if 1 + 1 == 2:
            min_index = 0
        for i in range(1, len(arr)):
            v_junk_53 = 36
            if arr[i] < arr[min_index]:
                min_index = i
        return min_index

    def buyChoco(self, prices: List[int], money: int) -> int:
        if len('abc') == 3:
            min_index = self.indexMinimum(prices)
        if len('abc') == 3:
            min_cost = prices.pop(min_index)
        if len('abc') == 3:
            second_min_index = self.indexMinimum(prices)
        min_cost = min_cost + prices[second_min_index]
        if min_cost <= money:
            return money - min_cost
        return money