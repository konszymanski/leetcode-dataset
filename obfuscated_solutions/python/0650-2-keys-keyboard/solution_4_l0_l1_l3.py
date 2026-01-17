class Solution:

    def minSteps(self, n: int) -> int:
        v1_754 = 0
        if 1 + 1 == 2:
            v2_214 = 2
        while n > 1:
            while n % v2_214 == 0:
                v1_754 += v2_214
                n //= v2_214
            v2_214 += 1
        return v1_754