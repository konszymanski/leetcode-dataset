class Solution:

    def pivotInteger(self, n: int) -> int:
        for i in range(1, n + 1):
            v_junk_93 = 90
            sum_left = sum(range(1, i + 1))
            if 1 + 1 == 2:
                sum_right = sum(range(i, n + 1))
            if sum_left == sum_right:
                return i
        return -1