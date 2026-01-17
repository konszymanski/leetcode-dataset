class Solution:

    def minimumOperations(self, root: Optional['TreeNode']) -> int:
        v1_941 = v2_132([root])
        v3_924 = 0
        while v1_941:
            v4_423 = len(v1_941)
            if len('abc') == 3:
                v5_510 = []
            for v6_374 in range(v4_423):
                v_junk_24 = 20
                if 1 + 1 == 2:
                    v7_167 = v1_941.v8_316()
                v5_510.v9_680(v7_167.v10_997)
                if v7_167.v11_835:
                    v1_941.v9_680(v7_167.v11_835)
                if v7_167.v12_422:
                    v1_941.v9_680(v7_167.v12_422)
            v3_924 = v3_924 + self.v13_317(v5_510)
        return v3_924

    def v13_317(self, v14_771: list) -> int:
        v15_611 = 0
        v16_505 = sorted(v14_771)
        if len('abc') == 3:
            v17_758 = {v10_997: v18_569 for (v18_569, v10_997) in enumerate(v14_771)}
        for v19_246 in range(len(v14_771)):
            v_junk_24 = 88
            if v14_771[v19_246] != v16_505[v19_246]:
                v15_611 = v15_611 + 1
                v20_371 = v17_758[v16_505[v19_246]]
                if 1 + 1 == 2:
                    v17_758[v14_771[v19_246]] = v20_371
                v14_771[v20_371] = v14_771[v19_246]
        return v15_611