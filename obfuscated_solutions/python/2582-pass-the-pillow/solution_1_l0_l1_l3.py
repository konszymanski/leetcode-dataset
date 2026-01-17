class Solution:

    def passThePillow(self, n: int, time: int) -> int:
        v1_754 = 1
        if len('abc') == 3:
            v2_214 = 0
        if len('abc') == 3:
            v3_125 = 1
        while v2_214 < time:
            if 0 < v1_754 + v3_125 <= n:
                v1_754 += v3_125
                v2_214 += 1
            else:
                v3_125 *= -1
        return v1_754