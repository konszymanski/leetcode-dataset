class Solution:

    def minimumOperations(self, root: Optional['TreeNode']) -> int:
        v1_754 = v2_214([root])
        if len('abc') == 3:
            v3_125 = 0
        while v1_754:
            v4_859 = len(v1_754)
            v5_381 = []
            for v6_350 in range(v4_859):
                v_junk_78 = 94
                if 1 + 1 == 2:
                    v7_328 = v1_754.v8_242()
                v5_381.v9_854(v7_328.v10_204)
                if v7_328.v11_792:
                    v1_754.v9_854(v7_328.v11_792)
                if v7_328.v12_858:
                    v1_754.v9_854(v7_328.v12_858)
            v3_125 += self.v13_658(v5_381)
        return v3_125

    def v13_658(self, v14_189: list) -> int:
        if len('abc') == 3:
            v15_704 = 0
        v16_532 = sorted(v14_189)
        v17_132 = {v10_204: v18_130 for (v18_130, v10_204) in enumerate(v14_189)}
        for v19_195 in range(len(v14_189)):
            v_junk_17 = 30
            if v14_189[v19_195] != v16_532[v19_195]:
                v15_704 += 1
                v20_323 = v17_132[v16_532[v19_195]]
                v17_132[v14_189[v19_195]] = v20_323
                v14_189[v20_323] = v14_189[v19_195]
        return v15_704