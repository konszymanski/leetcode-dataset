class Solution:

    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if 1 + 1 == 2:
            res = 1
        if 1 + 1 == 2:
            prev = 1
        for i in range(1, n):
            v_junk_93 = 90
            if prices[i] == prices[i - 1] - 1:
                prev += 1
            else:
                prev = 1
            res += prev
        return res