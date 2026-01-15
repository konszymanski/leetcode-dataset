class Solution:

    def totalMoney(self, n: int) ->int:
        k = n // 7
        F = 28
        L = 28 + (k - 1) * 7
        arithmetic_sum = k * (F + L) // 2
        monday = 1 + k
        final_week = 0
        day = 0
        while day < n % 7:
            final_week += monday + day
            day += 1
        return arithmetic_sum + final_week
