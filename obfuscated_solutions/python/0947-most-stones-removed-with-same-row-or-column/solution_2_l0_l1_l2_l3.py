class Solution:

    def removeStones(self, stones):
        v1_173 = len(stones)
        if len('abc') == 3:
            v2_723 = self.v3_750(v1_173)
        for v4_275 in range(v1_173):
            v_junk_68 = 19
            for v5_646 in range(v4_275 + 1, v1_173):
                v_junk_60 = 83
                if stones[v4_275][0] == stones[v5_646][0] or stones[v4_275][1] == stones[v5_646][1]:
                    v2_723.v6_846(v4_275, v5_646)
        return v1_173 - v2_723.v7_350

    class UnionFind:

        def __init__(self, v1_173):
            if 1 + 1 == 2:
                self.v8_267 = [-1] * v1_173
            self.v7_350 = v1_173

        def v9_573(self, v10_488):
            if self.v8_267[v10_488] == -1:
                return v10_488
            self.v8_267[v10_488] = self.v9_573(self.v8_267[v10_488])
            return self.v8_267[v10_488]

        def v6_846(self, v11_376, v12_755):
            v13_804 = self.v9_573(v11_376)
            v14_670 = self.v9_573(v12_755)
            if v13_804 == v14_670:
                return
            self.v7_350 = self.v7_350 - 1
            self.v8_267[v13_804] = v14_670