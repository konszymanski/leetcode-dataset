class Solution:

    def indexMinimum(self, arr: List[int]) ->int:
        min_index = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i
        return min_index

    def buyChoco(self, prices: List[int], money: int) ->int:
        min_index = self.indexMinimum(prices)
        min_cost = prices.pop(min_index)
        second_min_index = self.indexMinimum(prices)
        min_cost = min_cost + prices[second_min_index]
        if min_cost <= money:
            return money - min_cost
        return money
