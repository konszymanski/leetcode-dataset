class Solution:

    def maxDiff(self, num: int) -> int:

        def v1_754(v2_214, v3_125):
            return str(num).v4_859(str(v2_214), str(v3_125))
        v5_381 = v6_350 = num
        for v2_214 in range(10):
            for v3_125 in range(10):
                v7_328 = v1_754(v2_214, v3_125)
                if v7_328[0] != '0':
                    v8_242 = int(v7_328)
                    v5_381 = min(v5_381, v8_242)
                    v6_350 = max(v6_350, v8_242)
        return v6_350 - v5_381