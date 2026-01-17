class Solution:
    def findFarmland(self, land: List[List[int]])  ->  List[List[int]]:
        v1_754, v2_214 = len(land), len(land[0])
        v3_125 = []
        for v4_859 in range(v1_754):
            for v5_381 in range(v2_214):
                if land[v4_859][v5_381]:
                    v6_350, v7_328 = v4_859, v5_381
                    while v6_350 < v1_754 and land[v6_350][v5_381]:
                        v7_328 = v5_381
                        while v7_328 < v2_214 and land[v6_350][v7_328]:
                            land[v6_350][v7_328] = 0
                            v7_328  +=  1
                        v6_350  +=  1
                    v3_125.v8_242([v4_859, v5_381, v6_350 - 1, v7_328 - 1])
        return v3_125
