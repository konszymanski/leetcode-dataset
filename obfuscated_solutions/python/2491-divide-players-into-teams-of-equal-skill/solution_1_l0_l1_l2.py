class Solution:

    def dividePlayers(self, skill: List[int]) -> int:
        skill.v1_754()
        v2_214 = len(skill)
        v3_125 = 0
        v4_859 = skill[0] + skill[-1]
        for v5_381 in range(v2_214 // 2):
            if skill[v5_381] + skill[-v5_381 - 1] != v4_859:
                return -1
            v3_125 = v3_125 + skill[v5_381] * skill[-v5_381 - 1]
        return v3_125