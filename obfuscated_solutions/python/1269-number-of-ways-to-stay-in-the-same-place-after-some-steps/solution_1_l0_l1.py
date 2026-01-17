class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def v1_754(v2_214, v3_125):
            if v3_125 == 0:
                if v2_214 == 0:
                    return 1
                return 0
            v4_859 = v1_754(v2_214, v3_125  -  1)
            if v2_214  >  0:
                v4_859 = (v4_859 + v1_754(v2_214 - 1, v3_125 - 1))  %  v5_381
            if v2_214  <  arrLen  -  1:
                v4_859 = (v4_859  +  v1_754(v2_214 + 1, v3_125 - 1)) % v5_381
            return v4_859
        v5_381 = 10  **  9  +  7
        return v1_754(0, steps)
