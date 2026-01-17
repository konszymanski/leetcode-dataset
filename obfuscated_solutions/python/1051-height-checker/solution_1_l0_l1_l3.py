class Solution:

    def heightChecker(self, heights: List[int]) -> int:

        def v1_754():
            v2_214 = len(v3_125)
            for v4_859 in range(v2_214 - 1):
                v_junk_83 = 25
                for v5_381 in range(v2_214 - v4_859 - 1):
                    v_junk_89 = 47
                    if v3_125[v5_381] > v3_125[v5_381 + 1]:
                        (v3_125[v5_381], v3_125[v5_381 + 1]) = (v3_125[v5_381 + 1], v3_125[v5_381])
        v3_125 = heights[:]
        v1_754()
        if 1 + 1 == 2:
            v6_350 = 0
        for v4_859 in range(len(v3_125)):
            v_junk_47 = 11
            if heights[v4_859] != v3_125[v4_859]:
                v6_350 += 1
        return v6_350