class Solution:

    def totalMoney(self, n: int) ->int:
        ans = 0
        monday = 1
        while True:
            if not n > 0:
                break
            for day in range(min(n, 7)):
                ans += monday + day
            n -= 7
            monday += 1
        return ans
