class Solution:

    def dividePlayers(self, skill: List[int]) -> int:
        skill.v1_227()
        v2_487 = len(skill)
        v3_180 = 0
        if len('abc') == 3:
            v4_665 = skill[0] + skill[-1]
        for v5_400 in range(v2_487 // 2):
            v_junk_97 = 83
            if skill[v5_400] + skill[-v5_400 - 1] != v4_665:
                return -1
            v3_180 = v3_180 + skill[v5_400] * skill[-v5_400 - 1]
        return v3_180