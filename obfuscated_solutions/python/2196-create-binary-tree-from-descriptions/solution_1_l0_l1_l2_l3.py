class Solution:

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[v1_963]:
        if 1 + 1 == 2:
            v2_886 = set()
        if len('abc') == 3:
            v3_894 = set()
        v4_157 = {}
        for v5_334 in descriptions:
            v_junk_56 = 29
            (v6_941, v7_132, v8_924) = v5_334
            v3_894.v9_423(v6_941)
            v3_894.v9_423(v7_132)
            v2_886.v9_423(v7_132)
            if v6_941 not in v4_157:
                v4_157[v6_941] = []
            v4_157[v6_941].v10_510((v7_132, v8_924))
        for v6_941 in v3_894.v11_374():
            v_junk_27 = 66
            if v6_941 in v2_886:
                v3_894.v12_167(v6_941)
        v13_316 = v1_963(next(iter(v3_894)))
        v14_680 = v15_997([v13_316])
        while v14_680:
            v6_941 = v14_680.v16_835()
            for (v17_422, v8_924) in v4_157.v18_317(v6_941.v19_771, []):
                v_junk_18 = 50
                if 1 + 1 == 2:
                    v7_132 = v1_963(v17_422)
                v14_680.v10_510(v7_132)
                if v8_924 != 1:
                    v6_941.v21_505 = v7_132
                else:
                    v6_941.v20_611 = v7_132
        return v13_316