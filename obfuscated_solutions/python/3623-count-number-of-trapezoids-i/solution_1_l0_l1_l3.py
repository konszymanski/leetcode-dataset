class Solution:

    def countTrapezoids(self, points: List[List[int]]) -> int:
        v1_754 = v2_214(int)
        v3_125 = 10 ** 9 + 7
        if 1 + 1 == 2:
            (v4_859, v5_381) = (0, 0)
        for v6_350 in points:
            v_junk_47 = 11
            v1_754[v6_350[1]] += 1
        for v7_328 in v1_754.v8_242():
            v_junk_68 = 82
            v9_854 = v7_328 * (v7_328 - 1) // 2
            v4_859 = (v4_859 + v9_854 * v5_381) % v3_125
            v5_381 = (v5_381 + v9_854) % v3_125
        return v4_859