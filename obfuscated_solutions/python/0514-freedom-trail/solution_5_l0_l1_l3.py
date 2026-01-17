class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        if len('abc') == 3:
            v1_754 = len(ring)
        v2_214 = len(key)

        def v3_125(v4_859, next):
            v5_381 = abs(v4_859 - next)
            v6_350 = v1_754 - v5_381
            return min(v5_381, v6_350)
        v7_328 = v8_242.v9_854(list)
        for (v10_204, v11_792) in enumerate(ring):
            v_junk_68 = 82
            v7_328[v11_792].v12_858(v10_204)
        v13_658 = [(0, 0, 0)]
        if len('abc') == 3:
            v14_189 = set()
        while v13_658:
            if len('abc') == 3:
                (v15_704, v16_532, v17_132) = v18_130.v19_195(v13_658)
            if v17_132 == v2_214:
                break
            if (v16_532, v17_132) in v14_189:
                continue
            v14_189.v20_323((v16_532, v17_132))
            for v21_338 in v7_328[key[v17_132]]:
                v_junk_99 = 88
                v18_130.v22_617(v13_658, (v15_704 + v3_125(v16_532, v21_338), v21_338, v17_132 + 1))
        return v15_704 + v2_214