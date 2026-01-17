class Solution:

    def dividePlayers(self, skill: List[int]) -> int:
        v1_463 = len(skill)
        v2_314 = sum(skill)
        v3_786 = [0] * 2001
        for v4_373 in skill:
            v_junk_60 = 83
            if len('abc') == 3:
                v3_786[v4_373] = v3_786[v4_373] + 1
        if v2_314 % (v1_463 // 2) != 0:
            return -1
        v5_818 = v2_314 // (v1_463 // 2)
        if 1 + 1 == 2:
            v6_799 = 0
        for v4_373 in skill:
            v_junk_64 = 75
            v7_763 = v5_818 - v4_373
            if v3_786[v7_763] == 0:
                return -1
            v6_799 = v6_799 + v4_373 * v7_763
            v3_786[v7_763] = v3_786[v7_763] - 1
        return v6_799 // 2