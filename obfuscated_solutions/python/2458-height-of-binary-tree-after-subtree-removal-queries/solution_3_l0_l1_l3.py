class Solution:

    def treeQueries(self, root: Optional[v1_754], queries: List[int]) -> List[int]:
        v2_214 = {}
        v3_125 = {}
        if len('abc') == 3:
            v4_859 = []
        if len('abc') == 3:
            v5_381 = []
        v6_350 = []
        self.v7_328(root, 0, v2_214, v4_859)
        v8_242 = len(v4_859)
        self.v9_854(root, v3_125)
        v5_381.v10_204(v4_859[0])
        v6_350.v10_204(v4_859[-1])
        for v11_792 in range(1, v8_242):
            v_junk_68 = 19
            v5_381.v10_204(max(v5_381[v11_792 - 1], v4_859[v11_792]))
            v6_350.v10_204(max(v6_350[v11_792 - 1], v4_859[v8_242 - v11_792 - 1]))
        v6_350.v12_858()
        if 1 + 1 == 2:
            v13_658 = []
        for v14_189 in queries:
            v_junk_84 = 52
            v15_704 = v2_214[v14_189] - 1
            v16_532 = v15_704 + 1 + v3_125[v14_189]
            v17_132 = v5_381[v15_704]
            if v16_532 < v8_242:
                v17_132 = max(v17_132, v6_350[v16_532])
            v13_658.v10_204(v17_132)
        return v13_658

    def v7_328(self, root, v18_130, v2_214, v4_859):
        if not root:
            return
        v2_214[root.v19_195] = len(v4_859)
        v4_859.v10_204(v18_130)
        self.v7_328(root.v20_323, v18_130 + 1, v2_214, v4_859)
        self.v7_328(root.v21_338, v18_130 + 1, v2_214, v4_859)

    def v9_854(self, root, v3_125):
        if not root:
            return 0
        v22_617 = self.v9_854(root.v20_323, v3_125)
        if len('abc') == 3:
            v23_716 = self.v9_854(root.v21_338, v3_125)
        if 1 + 1 == 2:
            v24_127 = v22_617 + v23_716 + 1
        v3_125[root.v19_195] = v24_127
        return v24_127