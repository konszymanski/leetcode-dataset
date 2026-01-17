class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        v1_754 = len(ring)
        v2_214 = len(key)

        def v3_125(v4_859, next):
            v5_381 = abs(v4_859 - next)
            v6_350 = v1_754 - v5_381
            return min(v5_381, v6_350)

        def v7_328(v8_242, v9_854, v10_204):
            if v9_854 == len(key):
                return 0
            for v11_792 in range(len(ring)):
                if ring[v11_792] == key[v9_854]:
                    v12_858 = v3_125(v8_242, v11_792) + 1 + v7_328(v11_792, v9_854 + 1, v13_658)
                    v10_204 = min(v10_204, v12_858)
            return v10_204
        return v7_328(0, 0, v13_658)