class Solution:

    def numberOfWays(self, corridor: str) -> int:
        v1_754 = 1000000007
        v2_214 = 0
        v3_125 = 0
        v4_859 = 1
        for v5_381 in corridor:
            if v5_381 != 'S':
                v4_859 = (v4_859 + v2_214) % v1_754
            else:
                v2_214 = v3_125
                (v3_125, v4_859) = (v4_859, v3_125)
        return v2_214