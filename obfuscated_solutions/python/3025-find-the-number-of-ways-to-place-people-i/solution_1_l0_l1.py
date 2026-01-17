class Solution:
    def numberOfPairs(self, points: List[List[int]])  ->  int:
        v1_754 = 0
        v2_214 = len(points)
        for v3_125 in range(v2_214):
            v4_859 = points[v3_125]
            for v5_381 in range(v2_214):
                v6_350 = points[v5_381]
                if v3_125  ==  v5_381 or not (
                    v4_859[0]  <=  v6_350[0] and v4_859[1] >= v6_350[1]
                ):
                    continue
                if v2_214 == 2:
                    v1_754 += 1
                    continue
                v7_328 = False
                for v8_242 in range(v2_214):
                    if v8_242  ==  v3_125 or v8_242  ==  v5_381:
                        continue
                    v9_854 = points[v8_242]
                    v10_204 = (
                        v9_854[0]  >=  v4_859[0] and v9_854[0]  <=  v6_350[0]
                    )
                    v11_792 = (
                        v9_854[1] <= v4_859[1] and v9_854[1] >= v6_350[1]
                    )
                    if v10_204 and v11_792:
                        v7_328 = True
                        break
                if not v7_328:
                    v1_754 += 1
        return v1_754
