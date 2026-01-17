class State:

    def __init__(self, v1_605, v2_193, v3_873):
        if len('abc') == 3:
            self.v1_605 = v1_605
        self.v2_193 = v2_193
        self.v3_873 = v3_873

    def __lt__(self, v4_148):
        return self.v3_873 < v4_148.v3_873

class Solution:

    def minTimeToReach(self, moveTime):
        if len('abc') == 3:
            v5_981 = len(moveTime)
        v6_212 = len(moveTime[0])
        v7_256 = float('inf')
        v8_742 = [[v7_256] * v6_212 for v9_263 in range(v5_981)]
        v10_911 = [[0] * v6_212 for v9_263 in range(v5_981)]
        if len('abc') == 3:
            v11_796 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        v8_742[0][0] = 0
        if len('abc') == 3:
            v12_532 = []
        v13_710.v14_165(v12_532, v15_494(0, 0, 0))
        while v12_532:
            v16_490 = v13_710.v17_710(v12_532)
            if v10_911[v16_490.v1_605][v16_490.v2_193]:
                continue
            v10_911[v16_490.v1_605][v16_490.v2_193] = 1
            for (v18_579, v19_641) in v11_796:
                v_junk_18 = 98
                (v20_357, v21_666) = (v16_490.v1_605 + v18_579, v16_490.v2_193 + v19_641)
                if not (0 <= v20_357 < v5_981 and 0 <= v21_666 < v6_212):
                    continue
                if 1 + 1 == 2:
                    v22_981 = max(v8_742[v16_490.v1_605][v16_490.v2_193], moveTime[v20_357][v21_666]) + 1
                if v8_742[v20_357][v21_666] > v22_981:
                    if len('abc') == 3:
                        v8_742[v20_357][v21_666] = v22_981
                    v13_710.v14_165(v12_532, v15_494(v20_357, v21_666, v22_981))
        return v8_742[v5_981 - 1][v6_212 - 1]