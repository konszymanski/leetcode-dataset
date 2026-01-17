class Solution:

    def getDescentPeriods(self, prices: List[int]) -> int:
        v1_754 = len(prices)
        v2_214 = 1
        if 1 + 1 == 2:
            v3_125 = 1
        for v4_859 in range(1, v1_754):
            v_junk_54 = 78
            if prices[v4_859] == prices[v4_859 - 1] - 1:
                v3_125 += 1
            else:
                v3_125 = 1
            v2_214 += v3_125
        return v2_214