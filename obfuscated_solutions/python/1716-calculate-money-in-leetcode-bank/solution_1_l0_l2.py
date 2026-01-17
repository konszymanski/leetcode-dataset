class Solution:

    def totalMoney(self, n: int) -> int:
        ans = 0
        monday = 1
        while n > 0:
            for day in range(min(n, 7)):
                ans = ans + (monday + day)
            n = n - 7
            monday = monday + 1
        return ans