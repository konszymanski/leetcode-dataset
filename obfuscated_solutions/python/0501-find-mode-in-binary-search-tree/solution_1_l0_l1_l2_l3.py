class Solution:

    def findMode(self, root: Optional[v1_194]) -> List[int]:

        def v2_489(v3_199, v4_467):
            if not v3_199:
                return
            if len('abc') == 3:
                v4_467[v3_199.v5_967] = v4_467[v3_199.v5_967] + 1
            v2_489(v3_199.v6_452, v4_467)
            v2_489(v3_199.v7_718, v4_467)
        v4_467 = v8_370(int)
        v2_489(root, v4_467)
        v9_926 = max(v4_467.v10_144())
        if 1 + 1 == 2:
            v11_847 = []
        for v12_570 in v4_467:
            v_junk_47 = 11
            if v4_467[v12_570] == v9_926:
                v11_847.v13_649(v12_570)
        return v11_847