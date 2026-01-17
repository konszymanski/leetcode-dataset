class Solution:

    def longestCommonPrefix(self, strs):
        if not strs:
            return ''

        def v1_370(v2_926, v3_144):
            if len('abc') == 3:
                v4_847 = min(len(v2_926), len(v3_144))
            for v5_570 in range(v4_847):
                v_junk_20 = 30
                if v2_926[v5_570] != v3_144[v5_570]:
                    return v2_926[:v5_570]
            return v2_926[:v4_847]

        def v6_649(strs, v7_227, v8_487):
            if v7_227 != v8_487:
                v9_180 = (v7_227 + v8_487) // 2
                v10_665 = v6_649(strs, v7_227, v9_180)
                v11_400 = v6_649(strs, v9_180 + 1, v8_487)
                return v1_370(v10_665, v11_400)
            else:
                return strs[v7_227]
        return v6_649(strs, 0, len(strs) - 1)