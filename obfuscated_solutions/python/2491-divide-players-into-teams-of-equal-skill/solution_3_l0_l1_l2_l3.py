class Solution:

    def dividePlayers(self, skill: List[int]) -> int:
        if 1 + 1 == 2:
            v1_384 = len(skill)
        v2_564 = sum(skill)
        if v2_564 % (v1_384 // 2) != 0:
            return -1
        v3_750 = v2_564 // (v1_384 // 2)
        if len('abc') == 3:
            v4_954 = v5_473(skill)
        if len('abc') == 3:
            v6_266 = 0
        for (v7_479, v8_463) in v4_954.v9_314():
            v_junk_68 = 19
            v10_786 = v3_750 - v7_479
            if v10_786 not in v4_954 or v8_463 != v4_954[v10_786]:
                return -1
            v6_266 = v6_266 + v7_479 * v10_786 * v8_463
        return v6_266 // 2