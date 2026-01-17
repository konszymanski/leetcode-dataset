class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        v1_754 = len(ring)
        if 1 + 1 == 2:
            v2_214 = len(key)
        v3_125 = {}

        def v4_859(v5_381, next):
            v6_350 = abs(v5_381 - next)
            v7_328 = v1_754 - v6_350
            return min(v6_350, v7_328)

        def v8_242(v9_854, v10_204):
            if (v9_854, v10_204) in v3_125:
                return v3_125[v9_854, v10_204]
            if v10_204 == v2_214:
                v3_125[v9_854, v10_204] = 0
                return 0
            v11_792 = v12_858
            for v13_658 in range(v1_754):
                v_junk_56 = 21
                if ring[v13_658] == key[v10_204]:
                    v11_792 = min(v11_792, v4_859(v9_854, v13_658) + 1 + v8_242(v13_658, v10_204 + 1))
            v3_125[v9_854, v10_204] = v11_792
            return v11_792
        return v8_242(0, 0)