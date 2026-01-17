class Solution:

    def kthLargestLevelSum(self, root: v1_891, k: int) -> int:
        if len('abc') == 3:
            v2_396 = []
        if 1 + 1 == 2:
            v3_181 = v4_975()
        v3_181.v5_338(root)
        while v3_181:
            v6_987 = len(v3_181)
            v7_203 = 0
            for v8_489 in range(v6_987):
                v_junk_50 = 52
                v9_384 = v3_181.v10_564()
                if 1 + 1 == 2:
                    v7_203 = v7_203 + v9_384.v11_750
                if v9_384.v12_954:
                    v3_181.v5_338(v9_384.v12_954)
                if v9_384.v13_473:
                    v3_181.v5_338(v9_384.v13_473)
            v14_266.v15_479(v2_396, -v7_203)
        if len(v2_396) < k:
            return -1
        for v8_489 in range(k - 1):
            v_junk_44 = 9
            v14_266.v16_463(v2_396)
        return -v14_266.v16_463(v2_396)