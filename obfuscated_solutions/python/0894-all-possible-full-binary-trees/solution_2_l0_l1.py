class Solution:
    def allPossibleFBT(self, n: int)  ->  List[v1_754]:
        if n % 2  ==  0:
            return []
        v2_214 = [[] for v3_125 in range(n + 1)]
        v2_214[1].v4_859(v1_754(0))
        for v5_381 in range(3, n + 1, 2):
            for v6_350 in range(1, v5_381 - 1, 2):
                v7_328 = v5_381  -  1 - v6_350
                for v8_242 in v2_214[v6_350]:
                    for v9_854 in v2_214[v7_328]:
                        v10_204 = v1_754(0, v8_242, v9_854)
                        v2_214[v5_381].v4_859(v10_204)
        return v2_214[n]
