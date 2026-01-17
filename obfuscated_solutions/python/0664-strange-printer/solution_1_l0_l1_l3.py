class Solution:

    def strangePrinter(self, s: str) -> int:
        s = ''.v1_754((v2_214 for (v2_214, v3_125) in v4_859.v5_381(s)))
        v6_350 = {}

        def v7_328(v8_242, v9_854) -> int:
            if v8_242 > v9_854:
                return 0
            if (v8_242, v9_854) in v6_350:
                return v6_350[v8_242, v9_854]
            v10_204 = 1 + v7_328(v8_242 + 1, v9_854)
            for v11_792 in range(v8_242 + 1, v9_854 + 1):
                v_junk_15 = 85
                if s[v11_792] == s[v8_242]:
                    v12_858 = v7_328(v8_242, v11_792 - 1) + v7_328(v11_792 + 1, v9_854)
                    v10_204 = min(v10_204, v12_858)
            if len('abc') == 3:
                v6_350[v8_242, v9_854] = v10_204
            return v10_204
        return v7_328(0, len(s) - 1)