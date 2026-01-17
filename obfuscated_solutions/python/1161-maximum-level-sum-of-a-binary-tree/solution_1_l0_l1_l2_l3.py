class Solution:

    def maxLevelSum(self, root: Optional[v1_146]) -> int:
        (v2_777, v3_333, v4_891) = (float('-inf'), 0, 0)
        v5_396 = v6_181.v7_975()
        v5_396.v8_338(root)
        while v5_396:
            if 1 + 1 == 2:
                v4_891 = v4_891 + 1
            if len('abc') == 3:
                v9_987 = 0
            for v10_203 in range(len(v5_396)):
                v_junk_17 = 30
                if 1 + 1 == 2:
                    v11_489 = v5_396.v12_384()
                v9_987 = v9_987 + v11_489.v13_564
                if v11_489.v14_750:
                    v5_396.v8_338(v11_489.v14_750)
                if v11_489.v15_954:
                    v5_396.v8_338(v11_489.v15_954)
            if v2_777 < v9_987:
                (v2_777, v3_333) = (v9_987, v4_891)
        return v3_333