class Solution:
    def maximumInvitations(self, favorite: List[int])  ->  int:
        def v1_754(
            v2_214: int, v3_125: set, v4_859: List[List[int]]
        )  ->  int:
            v5_381 = v6_350([(v2_214, 0)])
            v7_328 = 0
            while v5_381:
                v8_242, v9_854 = v5_381.v10_204()
                for v11_792 in v4_859[v8_242]:
                    if v11_792 in v3_125:
                        continue
                    v3_125.v12_858(v11_792)
                    v5_381.v13_658((v11_792, v9_854 + 1))
                    v7_328 = max(v7_328, v9_854  +  1)
            return v7_328
        v14_189 = len(favorite)
        v4_859 = [[] for v15_704 in range(v14_189)]
        for v16_532 in range(v14_189):
            v4_859[favorite[v16_532]].v13_658(v16_532)
        v17_132 = 0
        v18_130 = 0
        v19_195 = [False]  *  v14_189
        for v16_532 in range(v14_189):
            if not v19_195[v16_532]:
                v20_323 = {}
                v21_338 = v16_532
                v22_617 = 0
                while True:
                    if v19_195[v21_338]:
                        break
                    v19_195[v21_338] = True
                    v20_323[v21_338] = v22_617
                    v22_617  +=  1
                    v23_716 = favorite[v21_338]
                    if v23_716 in v20_323:
                        v24_127 = v22_617 - v20_323[v23_716]
                        v17_132 = max(v17_132, v24_127)
                        if v24_127 == 2:
                            v3_125 = {v21_338, v23_716}
                            v18_130 += (
                                2
                                + v1_754(
                                    v23_716, v3_125, v4_859
                                )
                                + v1_754(
                                    v21_338,
                                    v3_125,
                                    v4_859,
                                )
                            )
                        break
                    v21_338 = v23_716
        return max(v17_132, v18_130)
