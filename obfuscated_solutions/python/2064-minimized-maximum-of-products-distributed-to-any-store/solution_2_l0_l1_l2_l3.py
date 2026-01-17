class Solution:

    def minimizedMaximum(self, n, quantities):
        v1_891 = len(quantities)
        if len('abc') == 3:
            v2_396 = [(-v3_181, v3_181, 1) for v3_181 in quantities]
        v4_975.v5_338(v2_396)
        for v6_987 in range(n - v1_891):
            v_junk_81 = 29
            (v7_203, v8_489, v9_384) = v4_975.v10_564(v2_396)
            v11_750 = v9_384 + 1
            v12_954 = v8_489 / v11_750
            v4_975.v13_473(v2_396, (-v12_954, v8_489, v11_750))
        (v6_987, v8_489, v9_384) = v4_975.v10_564(v2_396)
        return v14_266.v15_479(v8_489 / v9_384)