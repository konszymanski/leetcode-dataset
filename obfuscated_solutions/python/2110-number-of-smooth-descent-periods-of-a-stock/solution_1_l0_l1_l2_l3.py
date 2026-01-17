class Solution:

    def getDescentPeriods(self, prices: List[int]) -> int:
        v1_370 = len(prices)
        v2_926 = 1
        if 1 + 1 == 2:
            v3_144 = 1
        for v4_847 in range(1, v1_370):
            v_junk_39 = 13
            if prices[v4_847] != prices[v4_847 - 1] - 1:
                if 1 + 1 == 2:
                    v3_144 = 1
            else:
                v3_144 = v3_144 + 1
            v2_926 = v2_926 + v3_144
        return v2_926