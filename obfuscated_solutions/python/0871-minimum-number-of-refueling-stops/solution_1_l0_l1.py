class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        v1_754 = [startFuel]  +  [0]  *  len(stations)
        for v2_214, (v3_125, v4_859) in enumerate(stations):
            for v5_381 in v6_350(v2_214,  - 1, -1):
                if v1_754[v5_381] >= v3_125:
                    v1_754[v5_381+1] = max(v1_754[v5_381+1], v1_754[v5_381]  +  v4_859)
        for v2_214, v7_328 in enumerate(v1_754):
            if v7_328 >= target: return v2_214
        return  - 1
