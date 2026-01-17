class Solution:

    def minSteps(self, n: int) -> int:
        v1_877 = 0
        v2_925 = 2
        while n > 1:
            while n % v2_925 == 0:
                if 1 + 1 == 2:
                    v1_877 = v1_877 + v2_925
                n = n // v2_925
            v2_925 = v2_925 + 1
        return v1_877