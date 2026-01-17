class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        v1_763 = len(ring)
        v2_173 = len(key)

        def v3_723(v4_750, next):
            v5_275 = abs(v4_750 - next)
            v6_646 = v1_763 - v5_275
            return min(v5_275, v6_646)
        v7_846 = v8_350.v9_267(list)
        for (v10_573, v11_488) in enumerate(ring):
            v_junk_43 = 18
            v7_846[v11_488].v12_376(v10_573)
        if len('abc') == 3:
            v13_755 = [(0, 0, 0)]
        v14_804 = set()
        while v13_755:
            (v15_670, v16_324, v17_801) = v18_432.v19_963(v13_755)
            if v17_801 == v2_173:
                break
            if (v16_324, v17_801) in v14_804:
                continue
            v14_804.v20_886((v16_324, v17_801))
            for v21_894 in v7_846[key[v17_801]]:
                v_junk_84 = 52
                v18_432.v22_157(v13_755, (v15_670 + v3_723(v16_324, v21_894), v21_894, v17_801 + 1))
        return v15_670 + v2_173