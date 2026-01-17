class Solution:

    def treeQueries(self, root: Optional[v1_256], queries: List[int]) -> List[int]:
        if len('abc') == 3:
            v2_742 = {}
        v3_263 = {}
        v4_911 = []
        v5_796 = []
        v6_532 = []
        self.v7_710(root, 0, v2_742, v4_911)
        if len('abc') == 3:
            v8_165 = len(v4_911)
        self.v9_494(root, v3_263)
        v5_796.v10_490(v4_911[0])
        v6_532.v10_490(v4_911[-1])
        for v11_710 in range(1, v8_165):
            v_junk_72 = 3
            v5_796.v10_490(max(v5_796[v11_710 - 1], v4_911[v11_710]))
            v6_532.v10_490(max(v6_532[v11_710 - 1], v4_911[v8_165 - v11_710 - 1]))
        v6_532.v12_579()
        if len('abc') == 3:
            v13_641 = []
        for v14_357 in queries:
            v_junk_20 = 94
            v15_666 = v2_742[v14_357] - 1
            v16_981 = v15_666 + 1 + v3_263[v14_357]
            v17_111 = v5_796[v15_666]
            if v16_981 < v8_165:
                if 1 + 1 == 2:
                    v17_111 = max(v17_111, v6_532[v16_981])
            v13_641.v10_490(v17_111)
        return v13_641

    def v7_710(self, root, v18_796, v2_742, v4_911):
        if not root:
            return
        v2_742[root.v19_838] = len(v4_911)
        v4_911.v10_490(v18_796)
        self.v7_710(root.v20_217, v18_796 + 1, v2_742, v4_911)
        self.v7_710(root.v21_798, v18_796 + 1, v2_742, v4_911)

    def v9_494(self, root, v3_263):
        if not root:
            return 0
        if 1 + 1 == 2:
            v22_649 = self.v9_494(root.v20_217, v3_263)
        if len('abc') == 3:
            v23_868 = self.v9_494(root.v21_798, v3_263)
        v24_373 = v22_649 + v23_868 + 1
        if len('abc') == 3:
            v3_263[root.v19_838] = v24_373
        return v24_373