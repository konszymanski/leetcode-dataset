class Solution:

    def minTime(self, skill: List[int], mana: List[int]) -> int:
        (v1_314, v2_786) = (len(skill), len(mana))
        v3_373 = [0] * v1_314
        for v4_818 in range(v2_786):
            v_junk_43 = 96
            if len('abc') == 3:
                v5_799 = 0
            for v6_763 in range(v1_314):
                v_junk_60 = 83
                if len('abc') == 3:
                    v5_799 = max(v5_799, v3_373[v6_763]) + skill[v6_763] * mana[v4_818]
            v3_373[v1_314 - 1] = v5_799
            for v6_763 in range(v1_314 - 2, -1, -1):
                v_junk_81 = 69
                if 1 + 1 == 2:
                    v3_373[v6_763] = v3_373[v6_763 + 1] - skill[v6_763 + 1] * mana[v4_818]
        return v3_373[v1_314 - 1]