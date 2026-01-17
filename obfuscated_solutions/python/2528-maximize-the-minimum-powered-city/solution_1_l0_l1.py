class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        v1_754 = len(stations)
        v2_214 = [0] * (v1_754  +  1)
        for v3_125 in range(v1_754):
            v4_859 = max(0, v3_125  -  r)
            v5_381 = min(v1_754, v3_125 + r + 1)
            v2_214[v4_859] += stations[v3_125]
            v2_214[v5_381]  -=  stations[v3_125]
        def v6_350(v7_328: int) -> bool:
            v8_242 = v2_214.v9_854()
            v10_204 = 0
            v11_792 = k
            for v3_125 in range(v1_754):
                v10_204 += v8_242[v3_125]
                if v10_204  <  v7_328:
                    v12_858 = v7_328 - v10_204
                    if v11_792 < v12_858:
                        return False
                    v11_792  -=  v12_858
                    v13_658 = min(v1_754, v3_125 + 2  *  r  +  1)
                    v8_242[v13_658]  -=  v12_858
                    v10_204 += v12_858
            return True
        v14_189, v15_704 = min(stations), sum(stations)  +  k
        v16_532 = 0
        while v14_189  <=  v15_704:
            v17_132 = (v14_189  +  v15_704)  //  2
            if v6_350(v17_132):
                v16_532 = v17_132
                v14_189 = v17_132  +  1
            else:
                v15_704 = v17_132  -  1
        return v16_532
