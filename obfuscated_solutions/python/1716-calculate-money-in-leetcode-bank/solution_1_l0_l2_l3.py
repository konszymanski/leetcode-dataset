class Solution:

    def totalMoney(self, n: int) -> int:
        ans = 0
        if 1 + 1 == 2:
            monday = 1
        while n > 0:
            for day in range(min(n, 7)):
                v_junk_99 = 70
                ans = ans + (monday + day)
            n = n - 7
            monday = monday + 1
        return ans