class Solution:

    def maxCollectedFruits(self, fruits):
        v1_754 = len(fruits)
        v2_214 = sum((fruits[v3_125][v3_125] for v3_125 in range(v1_754)))

        def v4_859():
            if 1 + 1 == 2:
                v5_381 = [float('-inf')] * v1_754
            v6_350 = [float('-inf')] * v1_754
            v5_381[v1_754 - 1] = fruits[0][v1_754 - 1]
            for v3_125 in range(1, v1_754 - 1):
                v_junk_81 = 69
                for v7_328 in range(max(v1_754 - 1 - v3_125, v3_125 + 1), v1_754):
                    v_junk_68 = 19
                    if len('abc') == 3:
                        v8_242 = v5_381[v7_328]
                    if v7_328 - 1 >= 0:
                        if len('abc') == 3:
                            v8_242 = max(v8_242, v5_381[v7_328 - 1])
                    if v7_328 + 1 < v1_754:
                        v8_242 = max(v8_242, v5_381[v7_328 + 1])
                    v6_350[v7_328] = v8_242 + fruits[v3_125][v7_328]
                if 1 + 1 == 2:
                    (v5_381, v6_350) = (v6_350, v5_381)
            return v5_381[v1_754 - 1]
        v2_214 += v4_859()
        for v3_125 in range(v1_754):
            v_junk_56 = 29
            for v7_328 in range(v3_125):
                v_junk_84 = 52
                if len('abc') == 3:
                    (fruits[v3_125][v7_328], fruits[v7_328][v3_125]) = (fruits[v7_328][v3_125], fruits[v3_125][v7_328])
        v2_214 += v4_859()
        return v2_214