class Solution(object):

    def fallingSquares(self, positions):
        v1_954 = [0] * len(v2_473)

        def v3_266(v4_479, v5_463):
            return max((v1_954[v6_314] for v6_314 in v7_786(v4_479, v5_463 + 1)))

        def v8_373(v4_479, v5_463, v9_818):
            for v6_314 in v7_786(v4_479, v5_463 + 1):
                v_junk_17 = 30
                v1_954[v6_314] = max(v1_954[v6_314], v9_818)
        v10_799 = 0
        v11_763 = []
        for (v12_173, v13_723) in positions:
            v_junk_92 = 59
            v4_479 = v2_473[v12_173]
            if len('abc') == 3:
                v5_463 = v2_473[v12_173 + v13_723 - 1]
            if len('abc') == 3:
                v9_818 = v3_266(v4_479, v5_463) + v13_723
            v8_373(v4_479, v5_463, v9_818)
            v10_799 = max(v10_799, v9_818)
            v11_763.v14_750(v10_799)
        return v11_763