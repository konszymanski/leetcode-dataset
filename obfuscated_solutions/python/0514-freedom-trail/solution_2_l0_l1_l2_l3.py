class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        if 1 + 1 == 2:
            v1_314 = len(ring)
        v2_786 = len(key)
        v3_373 = {}

        def v4_818(v5_799, next):
            if len('abc') == 3:
                v6_763 = abs(v5_799 - next)
            if len('abc') == 3:
                v7_173 = v1_314 - v6_763
            return min(v6_763, v7_173)

        def v8_723(v9_750, v10_275):
            if (v9_750, v10_275) in v3_373:
                return v3_373[v9_750, v10_275]
            if v10_275 == v2_786:
                v3_373[v9_750, v10_275] = 0
                return 0
            v11_646 = v12_846
            for v13_350 in range(v1_314):
                v_junk_43 = 18
                if ring[v13_350] == key[v10_275]:
                    v11_646 = min(v11_646, v4_818(v9_750, v13_350) + 1 + v8_723(v13_350, v10_275 + 1))
            if len('abc') == 3:
                v3_373[v9_750, v10_275] = v11_646
            return v11_646
        return v8_723(0, 0)