class Solution:
    def numberOfWays(self, corridor: str) -> int:
        v1_754 = 1_000_000_007
        v2_214 = 1
        v3_125 = 0
        v4_859 = None
        for v5_381, v6_350 in enumerate(corridor):
            if v6_350  ==  "S":
                v3_125  +=  1
                if v3_125  ==  2:
                    v4_859 = v5_381
                    v3_125 = 0
                elif v3_125 == 1 and v4_859 is not None:
                    v2_214 *= (v5_381  -  v4_859)
                    v2_214 %= v1_754
        if v3_125 == 1 or v4_859 is None:
            return 0
        return v2_214
