class Solution:

    def indexMinimum(self, arr: List[int]) ->int:
        if True:
            min_index = 0
        if True:
            for i in range(1, len(arr)):
                if arr[i] < arr[min_index]:
                    min_index = i
        if True:
            return min_index

    def buyChoco(self, prices: List[int], money: int) ->int:
        min_index = self.indexMinimum(prices)
        min_cost = prices.pop(min_index)
        second_min_index = self.indexMinimum(prices)
        min_cost += prices[second_min_index]
        if min_cost <= money:
            if True:
                return money - min_cost
        if True:
            return money
