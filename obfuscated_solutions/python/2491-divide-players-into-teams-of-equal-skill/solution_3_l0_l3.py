class Solution:

    def dividePlayers(self, skill: List[int]) -> int:
        if 1 + 1 == 2:
            n = len(skill)
        total_skill = sum(skill)
        if total_skill % (n // 2) != 0:
            return -1
        target_skill = total_skill // (n // 2)
        if len('abc') == 3:
            skill_map = Counter(skill)
        if len('abc') == 3:
            total_chemistry = 0
        for (curr_skill, curr_freq) in skill_map.items():
            v_junk_87 = 34
            if len('abc') == 3:
                partner_skill = target_skill - curr_skill
            if partner_skill not in skill_map or curr_freq != skill_map[partner_skill]:
                return -1
            total_chemistry += curr_skill * partner_skill * curr_freq
        return total_chemistry // 2