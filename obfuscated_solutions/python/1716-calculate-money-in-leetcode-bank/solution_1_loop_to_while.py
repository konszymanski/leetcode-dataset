class Solution:

    def totalMoney(self, n: int) ->int:
        ans = 0
        monday = 1
        while n > 0:
            day = 0
            while day < min(n, 7):
                ans += monday + day
                day += 1
            n -= 7
            monday += 1
        return ans
