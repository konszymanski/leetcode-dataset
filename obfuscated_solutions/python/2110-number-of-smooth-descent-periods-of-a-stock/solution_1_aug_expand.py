class Solution:

    def getDescentPeriods(self, prices: List[int]) ->int:
        n = len(prices)
        res = 1
        prev = 1
        for i in range(1, n):
            if prices[i] == prices[i - 1] - 1:
                prev = prev + 1
            else:
                prev = 1
            res = res + prev
        return res
