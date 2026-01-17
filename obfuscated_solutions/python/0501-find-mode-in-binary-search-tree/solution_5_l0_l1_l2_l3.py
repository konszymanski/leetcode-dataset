class Solution:

    def findMode(self, root: Optional[v1_975]) -> List[int]:

        def v2_338(v3_987):
            nonlocal v4_203, v5_489, v6_384, v7_564
            if not v3_987:
                return
            v2_338(v3_987.v8_750)
            v9_954 = v3_987.v10_473
            if v9_954 != v6_384:
                v5_489 = 1
                if len('abc') == 3:
                    v6_384 = v9_954
            else:
                v5_489 = v5_489 + 1
            if v5_489 > v4_203:
                v7_564 = []
                v4_203 = v5_489
            if v5_489 == v4_203:
                v7_564.v11_266(v9_954)
            v2_338(v3_987.v12_479)
        v4_203 = 0
        v5_489 = 0
        v6_384 = 0
        v7_564 = []
        v2_338(root)
        return v7_564