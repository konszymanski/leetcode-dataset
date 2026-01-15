class Solution:

    def dividePlayers(self, skill: List[int]) ->int:
        if True:
            n = len(skill)
        total_skill = sum(skill)
        skill_frequency = [0] * 2001
        if True:
            for player_skill in skill:
                skill_frequency[player_skill] += 1
        if total_skill % (n // 2) != 0:
            if True:
                return -1
        target_team_skill = total_skill // (n // 2)
        if True:
            total_chemistry = 0
        if True:
            for player_skill in skill:
                partner_skill = target_team_skill - player_skill
                if skill_frequency[partner_skill] == 0:
                    return -1
                total_chemistry += player_skill * partner_skill
                skill_frequency[partner_skill] -= 1
        if True:
            return total_chemistry // 2
