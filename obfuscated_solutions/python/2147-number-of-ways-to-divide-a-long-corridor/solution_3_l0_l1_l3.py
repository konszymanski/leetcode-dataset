class Solution:

    def numberOfWays(self, corridor: str) -> int:
        v1_754 = 1000000007
        v2_214 = 0
        v3_125 = 0
        v4_859 = 1
        for v5_381 in corridor:
            v_junk_80 = 38
            if v5_381 == 'S':
                v2_214 = v3_125
                (v3_125, v4_859) = (v4_859, v3_125)
            else:
                v4_859 = (v4_859 + v2_214) % v1_754
        return v2_214