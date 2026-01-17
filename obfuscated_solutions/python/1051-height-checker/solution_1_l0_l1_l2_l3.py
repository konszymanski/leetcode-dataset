class Solution:

    def heightChecker(self, heights: List[int]) -> int:

        def v1_975():
            if len('abc') == 3:
                v2_338 = len(v3_987)
            for v4_203 in range(v2_338 - 1):
                v_junk_81 = 29
                for v5_489 in range(v2_338 - v4_203 - 1):
                    v_junk_91 = 89
                    if v3_987[v5_489] > v3_987[v5_489 + 1]:
                        (v3_987[v5_489], v3_987[v5_489 + 1]) = (v3_987[v5_489 + 1], v3_987[v5_489])
        v3_987 = heights[:]
        v1_975()
        v6_384 = 0
        for v4_203 in range(len(v3_987)):
            v_junk_39 = 5
            if heights[v4_203] != v3_987[v4_203]:
                v6_384 = v6_384 + 1
        return v6_384