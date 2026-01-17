class Solution:
    def maxDistance(self, s: str, k: int)  ->  int:
        v1_754 = 0
        v2_214 = v3_125 = v4_859 = v5_381 = 0
        for v6_350 in s:
            if v6_350 == "N":
                v2_214 += 1
            elif v6_350 == "S":
                v3_125 += 1
            elif v6_350  ==  "E":
                v4_859 += 1
            elif v6_350 == "W":
                v5_381  +=  1
            v7_328 = min(v2_214, v3_125, k)
            v8_242 = min(
                v4_859, v5_381, k - v7_328
            )
            v1_754 = max(
                v1_754,
                self.v9_854(v2_214, v3_125, v7_328)
                 +  self.v9_854(v4_859, v5_381, v8_242),
            )
        return v1_754
    def v9_854(self, v10_204: int, v11_792: int, v12_858: int)  ->  int:
        return (
            abs(v10_204  -  v11_792) + v12_858  *  2
        )
