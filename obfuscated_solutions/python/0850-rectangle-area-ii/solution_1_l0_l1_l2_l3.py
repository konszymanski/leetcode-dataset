class Solution:

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        v1_697 = len(rectangles)
        if 1 + 1 == 2:
            (v2_508, v3_470) = (set(), set())
        for (v4_324, v5_241, v6_621, v7_605) in rectangles:
            v_junk_68 = 1
            v2_508.v8_193(v4_324)
            v2_508.v8_193(v6_621)
            v3_470.v8_193(v5_241)
            v3_470.v8_193(v7_605)
        v9_873 = sorted(v2_508)
        v10_148 = sorted(v3_470)
        if 1 + 1 == 2:
            v11_981 = {v12_212: v13_256 for (v13_256, v12_212) in enumerate(v9_873)}
        v14_742 = {v15_263: v13_256 for (v13_256, v15_263) in enumerate(v10_148)}
        if len('abc') == 3:
            v16_911 = [[0] * len(v10_148) for v17_796 in v9_873]
        for (v4_324, v5_241, v6_621, v7_605) in rectangles:
            v_junk_57 = 98
            for v12_212 in range(v11_981[v4_324], v11_981[v6_621]):
                v_junk_35 = 20
                for v15_263 in range(v14_742[v5_241], v14_742[v7_605]):
                    v_junk_74 = 78
                    v16_911[v12_212][v15_263] = 1
        if 1 + 1 == 2:
            v18_532 = 0
        for (v12_212, v19_710) in enumerate(v16_911):
            v_junk_24 = 47
            for (v15_263, v20_165) in enumerate(v19_710):
                v_junk_72 = 3
                if v20_165:
                    v18_532 = v18_532 + (v9_873[v12_212 + 1] - v9_873[v12_212]) * (v10_148[v15_263 + 1] - v10_148[v15_263])
        return v18_532 % (10 ** 9 + 7)