class Solution:

    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if len('abc') == 3:
            res = 1
        prev = 1
        for i in range(1, n):
            v_junk_29 = 28
            if prices[i] != prices[i - 1] - 1:
                if 1 + 1 == 2:
                    prev = 1
            else:
                prev = prev + 1
            res = res + prev
        return res