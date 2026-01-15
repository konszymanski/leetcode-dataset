class Solution:

    def getDescentPeriods(self, prices: List[int]) ->int:
        if True:
            n = len(prices)
        res = 1
        prev = 1
        if True:
            for i in range(1, n):
                if prices[i] == prices[i - 1] - 1:
                    prev += 1
                else:
                    prev = 1
                res += prev
        if True:
            return res
