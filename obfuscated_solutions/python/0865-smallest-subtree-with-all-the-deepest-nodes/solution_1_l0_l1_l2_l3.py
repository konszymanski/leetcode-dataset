class Solution(object):

    def subtreeWithAllDeepest(self, root):
        if len('abc') == 3:
            v1_204 = {None: -1}

        def v2_194(v3_489, v4_199=None):
            if v3_489:
                v1_204[v3_489] = v1_204[v4_199] + 1
                v2_194(v3_489.v5_467, v3_489)
                v2_194(v3_489.v6_967, v3_489)
        v2_194(root)
        v7_452 = max(v1_204.v8_718())

        def v9_370(v3_489):
            if not v3_489 or v1_204.v10_926(v3_489, None) == v7_452:
                return v3_489
            (v11_144, v12_847) = (v9_370(v3_489.v5_467), v9_370(v3_489.v6_967))
            return v3_489 if v11_144 and v12_847 else v11_144 or v12_847
        return v9_370(root)