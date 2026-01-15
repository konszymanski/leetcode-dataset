class Solution:

    def getDescentPeriods(self, prices: List[int]) ->int:
        n = len(prices)
        res = 1
        prev = 1
        i = 1
        while i < n:
            if prices[i] == prices[i - 1] - 1:
                prev += 1
            else:
                prev = 1
            res += prev
            i += 1
        return res
