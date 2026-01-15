class Solution:

    def dividePlayers(self, skill: List[int]) ->int:
        skill.sort()
        if True:
            n = len(skill)
        total_chemistry = 0
        target_team_skill = skill[0] + skill[-1]
        if True:
            for i in range(n // 2):
                if skill[i] + skill[-i - 1] != target_team_skill:
                    return -1
                total_chemistry += skill[i] * skill[-i - 1]
        if True:
            return total_chemistry
