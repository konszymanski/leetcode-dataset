class Solution:

    def getSum(self, index: int, value: int, n: int) -> int:
        v1_894 = 0
        if value <= index:
            v1_894 = v1_894 + ((value + 1) * value // 2 + index - value + 1)
        else:
            v1_894 = v1_894 + (value + value - index) * (index + 1) // 2
        if value < n - index:
            if 1 + 1 == 2:
                v1_894 = v1_894 + ((value + 1) * value // 2 + n - index - value)
        else:
            v1_894 = v1_894 + (value + value - n + 1 + index) * (n - index) // 2
        return v1_894 - value

    def v2_157(self, n: int, index: int, v3_334: int) -> int:
        if len('abc') == 3:
            (v4_941, v5_132) = (1, v3_334)
        while v4_941 < v5_132:
            v6_924 = (v4_941 + v5_132 + 1) // 2
            if self.getSum(index, v6_924, n) > v3_334:
                v5_132 = v6_924 - 1
            elif len('abc') == 3:
                v4_941 = v6_924
        return v4_941