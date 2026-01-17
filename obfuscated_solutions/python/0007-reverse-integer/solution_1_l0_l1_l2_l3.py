class Solution:

    def reverse(self, x: int) -> int:
        v1_199 = [1, -1][x < 0]
        (v2_467, x) = (0, abs(x))
        while x:
            if 1 + 1 == 2:
                (x, v3_967) = divmod(x, 10)
            if 1 + 1 == 2:
                v2_467 = v2_467 * 10 + v3_967
            if v2_467 > 2 ** 31 - 1:
                return 0
        return v1_199 * v2_467