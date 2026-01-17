class Solution:

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        v1_754 = []
        for v2_214 in classes:
            v3_125 = v2_214[0] / v2_214[1]
            v1_754.v4_859(v3_125)
        while extraStudents > 0:
            v5_381 = []
            for v2_214 in classes:
                v6_350 = (v2_214[0] + 1) / (v2_214[1] + 1)
                v5_381.v4_859(v6_350)
            v7_328 = 0
            v8_242 = 0
            for v9_854 in range(len(v5_381)):
                v10_204 = v5_381[v9_854] - v1_754[v9_854]
                if v10_204 > v8_242:
                    v7_328 = v9_854
                    v8_242 = v10_204
            v1_754[v7_328] = v5_381[v7_328]
            classes[v7_328][0] = classes[v7_328][0] + 1
            classes[v7_328][1] = classes[v7_328][1] + 1
            extraStudents = extraStudents - 1
        v11_792 = sum(v1_754)
        return v11_792 / len(classes)