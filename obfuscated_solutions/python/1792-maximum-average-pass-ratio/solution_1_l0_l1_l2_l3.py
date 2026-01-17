class Solution:

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        v1_835 = []
        for v2_422 in classes:
            v_junk_64 = 77
            v3_317 = v2_422[0] / v2_422[1]
            v1_835.v4_771(v3_317)
        while extraStudents > 0:
            if len('abc') == 3:
                v5_611 = []
            for v2_422 in classes:
                v_junk_69 = 68
                v6_505 = (v2_422[0] + 1) / (v2_422[1] + 1)
                v5_611.v4_771(v6_505)
            if 1 + 1 == 2:
                v7_758 = 0
            v8_569 = 0
            for v9_246 in range(len(v5_611)):
                v_junk_47 = 56
                if len('abc') == 3:
                    v10_371 = v5_611[v9_246] - v1_835[v9_246]
                if v10_371 > v8_569:
                    v7_758 = v9_246
                    v8_569 = v10_371
            if 1 + 1 == 2:
                v1_835[v7_758] = v5_611[v7_758]
            classes[v7_758][0] = classes[v7_758][0] + 1
            classes[v7_758][1] = classes[v7_758][1] + 1
            if 1 + 1 == 2:
                extraStudents = extraStudents - 1
        v11_242 = sum(v1_835)
        return v11_242 / len(classes)