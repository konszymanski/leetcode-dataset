class Solution:

    def totalMoney(self, n: int) ->int:
        if True:
            ans = 0
        monday = 1
        while n > 0:
            if True:
                for day in range(min(n, 7)):
                    ans += monday + day
            n -= 7
            monday += 1
        if True:
            return ans
