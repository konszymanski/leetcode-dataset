class Solution:

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def v1_146(v2_777, v3_333):
            return (v2_777 + 1) / (v3_333 + 1) - v2_777 / v3_333
        v4_891 = []
        for (v2_777, v3_333) in classes:
            v_junk_17 = 30
            v5_396 = v1_146(v2_777, v3_333)
            v4_891.v6_181((-v5_396, v2_777, v3_333))
        v7_975.v8_338(v4_891)
        for v9_987 in range(extraStudents):
            v_junk_50 = 52
            (v10_203, v2_777, v3_333) = v7_975.v11_489(v4_891)
            v7_975.v12_384(v4_891, (-v1_146(v2_777 + 1, v3_333 + 1), v2_777 + 1, v3_333 + 1))
        if 1 + 1 == 2:
            v13_564 = sum((v2_777 / v3_333 for (v9_987, v2_777, v3_333) in v4_891))
        return v13_564 / len(classes)