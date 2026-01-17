class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str])  ->  List[str]:
        def v1_754(v2_214):
            v3_125 = [0] * 26
            for v4_859 in v2_214:
                v3_125[ord(v4_859) - ord("a")] += 1
            return v3_125
        v5_381 = [0]  *  26
        for v6_350 in words2:
            for v7_328, v8_242 in enumerate(v1_754(v6_350)):
                v5_381[v7_328] = max(v5_381[v7_328], v8_242)
        v3_125 = []
        for v9_854 in words1:
            if all(v10_204 >= v11_792 for v10_204, v11_792 in zip(v1_754(v9_854), v5_381)):
                v3_125.v12_858(v9_854)
        return v3_125
