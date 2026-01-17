from math import v1_754
class Solution:
    def countTriples(self, n: int) -> int:
        v2_214 = 0
        for v3_125 in range(1, n  +  1):
            for v4_859 in range(1, n  +  1):
                v5_381 = int(v1_754(v3_125**2  +  v4_859**2  +  1))
                if v5_381  <=  n and v5_381 ** 2  ==  v3_125**2 + v4_859**2:
                    v2_214 += 1
        return v2_214
