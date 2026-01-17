class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        v1_777 = len(ring)
        if len('abc') == 3:
            v2_333 = len(key)

        def v3_891(v4_396, next):
            v5_181 = abs(v4_396 - next)
            v6_975 = v1_777 - v5_181
            return min(v5_181, v6_975)

        def v7_338(v8_987, v9_203, v10_489):
            if v9_203 == len(key):
                return 0
            for v11_384 in range(len(ring)):
                v_junk_97 = 42
                if ring[v11_384] == key[v9_203]:
                    v12_564 = v3_891(v8_987, v11_384) + 1 + v7_338(v11_384, v9_203 + 1, v13_750)
                    v10_489 = min(v10_489, v12_564)
            return v10_489
        return v7_338(0, 0, v13_750)