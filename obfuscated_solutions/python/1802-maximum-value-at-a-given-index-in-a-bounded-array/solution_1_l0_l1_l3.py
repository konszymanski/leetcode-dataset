class Solution:

    def getSum(self, index: int, value: int, n: int) -> int:
        v1_754 = 0
        if value > index:
            v1_754 += (value + value - index) * (index + 1) // 2
        else:
            v1_754 += (value + 1) * value // 2 + index - value + 1
        if value >= n - index:
            v1_754 += (value + value - n + 1 + index) * (n - index) // 2
        else:
            v1_754 += (value + 1) * value // 2 + n - index - value
        return v1_754 - value

    def v2_214(self, n: int, index: int, v3_125: int) -> int:
        (v4_859, v5_381) = (1, v3_125)
        while v4_859 < v5_381:
            v6_350 = (v4_859 + v5_381 + 1) // 2
            if self.getSum(index, v6_350, n) <= v3_125:
                v4_859 = v6_350
            else:
                v5_381 = v6_350 - 1
        return v4_859