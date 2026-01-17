class Solution:

    def reverse(self, x: int) -> int:
        if len('abc') == 3:
            v1_754 = [1, -1][x < 0]
        (v2_214, x) = (0, abs(x))
        while x:
            if len('abc') == 3:
                (x, v3_125) = divmod(x, 10)
            if len('abc') == 3:
                v2_214 = v2_214 * 10 + v3_125
            if v2_214 > 2 ** 31 - 1:
                return 0
        return v1_754 * v2_214