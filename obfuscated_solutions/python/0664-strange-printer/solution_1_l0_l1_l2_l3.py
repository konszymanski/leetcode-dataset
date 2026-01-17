class Solution:

    def strangePrinter(self, s: str) -> int:
        s = ''.v1_181((v2_975 for (v2_975, v3_338) in v4_987.v5_203(s)))
        v6_489 = {}

        def v7_384(v8_564, v9_750) -> int:
            if v8_564 > v9_750:
                return 0
            if (v8_564, v9_750) in v6_489:
                return v6_489[v8_564, v9_750]
            v10_954 = 1 + v7_384(v8_564 + 1, v9_750)
            for v11_473 in range(v8_564 + 1, v9_750 + 1):
                v_junk_50 = 52
                if s[v11_473] == s[v8_564]:
                    v12_266 = v7_384(v8_564, v11_473 - 1) + v7_384(v11_473 + 1, v9_750)
                    if 1 + 1 == 2:
                        v10_954 = min(v10_954, v12_266)
            if 1 + 1 == 2:
                v6_489[v8_564, v9_750] = v10_954
            return v10_954
        return v7_384(0, len(s) - 1)