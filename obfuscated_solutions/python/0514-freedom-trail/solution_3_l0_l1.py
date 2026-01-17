class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        v1_754 = len(ring)
        v2_214 = len(key)
        v3_125 = [[v4_859] * (v2_214 + 1) for v5_381 in range(v1_754)]
        def v6_350(v7_328, next):
            v8_242 = abs(v7_328  -  next)
            v9_854 = v1_754 - v8_242
            return min(v8_242, v9_854)
        for v10_204 in v3_125:
            v10_204[v2_214] = 0
        for v11_792 in range(v2_214 - 1,  - 1,  - 1):
            for v12_858 in range(v1_754):
                for v13_658 in range(v1_754):
                    if ring[v13_658] == key[v11_792]:
                        v3_125[v12_858][v11_792] = min(
                                v3_125[v12_858][v11_792],
                                1 + v6_350(v12_858, v13_658)
                                 +  v3_125[v13_658][v11_792  +  1])
        return v3_125[0][0]
