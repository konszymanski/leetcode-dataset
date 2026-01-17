class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        v1_754 = len(ring)
        v2_214 = len(key)
        v3_125 = [v4_859 for v5_381 in range(v1_754)]
        v6_350 = [0 for v5_381 in range(v1_754)]

        def v7_328(v3_125, next):
            v8_242 = abs(v3_125 - next)
            v9_854 = v1_754 - v8_242
            return min(v8_242, v9_854)
        for v10_204 in range(v2_214 - 1, -1, -1):
            v3_125 = [v4_859 for v5_381 in range(v1_754)]
            for v11_792 in range(v1_754):
                for v12_858 in range(v1_754):
                    if ring[v12_858] == key[v10_204]:
                        v3_125[v11_792] = min(v3_125[v11_792], 1 + v7_328(v11_792, v12_858) + v6_350[v12_858])
            v6_350 = v3_125.v13_658()
        return v6_350[0]