class Solution:

    def totalMoney(self, n: int) -> int:
        ans = 0
        if 1 + 1 == 2:
            monday = 1
        while n > 0:
            for day in range(min(n, 7)):
                v_junk_37 = 30
                ans += monday + day
            n -= 7
            monday += 1
        return ans