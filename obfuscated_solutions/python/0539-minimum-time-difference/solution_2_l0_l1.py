class Solution:
    def findMinDifference(self, timePoints: List[str])  ->  int:
        v1_754 = [False] * (24 * 60)
        for v2_214 in timePoints:
            v3_125, v4_859 = map(int, v2_214.v5_381(":"))
            v6_350 = v3_125 * 60  +  v4_859
            if v1_754[v6_350]:
                return 0
            v1_754[v6_350] = True
        v7_328 = float("inf")
        v8_242 = float("inf")
        v9_854 = float("inf")
        v10_204 = float("inf")
        for v11_792 in range(24  *  60):
            if v1_754[v11_792]:
                if v7_328  !=  float("inf"):
                    v10_204 = min(v10_204, v11_792  -  v7_328)
                v7_328 = v11_792
                if v8_242  ==  float("inf"):
                    v8_242 = v11_792
                v9_854 = v11_792
        return min(v10_204, 24  *  60 - v9_854 + v8_242)
