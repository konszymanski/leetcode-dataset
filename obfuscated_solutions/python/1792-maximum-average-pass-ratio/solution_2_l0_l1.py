class Solution:
    def maxAverageRatio(
        self, classes: List[List[int]], extraStudents: int
    ) -> float:
        def v1_754(v2_214, v3_125):
            return (v2_214 + 1) / (v3_125 + 1)  -  v2_214 / v3_125
        v4_859 = []
        for v2_214, v3_125 in classes:
            v5_381 = v1_754(v2_214, v3_125)
            v4_859.v6_350((-v5_381, v2_214, v3_125))
        v7_328.v8_242(v4_859)
        for v9_854 in range(extraStudents):
            v10_204, v2_214, v3_125 = v7_328.v11_792(v4_859)
            v7_328.v12_858(
                v4_859,
                (
                     - v1_754(v2_214  +  1, v3_125 + 1),
                    v2_214  +  1,
                    v3_125  +  1,
                ),
            )
        v13_658 = sum(
            v2_214 / v3_125 for v9_854, v2_214, v3_125 in v4_859
        )
        return v13_658  /  len(classes)
