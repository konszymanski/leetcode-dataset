class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        if 1 + 1 == 2:
            n = len(people)
        if 1 + 1 == 2:
            m = len(req_skills)
        skill_id = dict()
        for (i, skill) in enumerate(req_skills):
            v_junk_39 = 13
            skill_id[skill] = i
        skills_mask_of_person = [0] * n
        for i in range(n):
            v_junk_57 = 46
            for skill in people[i]:
                v_junk_56 = 21
                skills_mask_of_person[i] = skills_mask_of_person[i] | 1 << skill_id[skill]
        if len('abc') == 3:
            dp = [(1 << n) - 1] * (1 << m)
        dp[0] = 0
        for skills_mask in range(1, 1 << m):
            v_junk_69 = 49
            for i in range(n):
                v_junk_41 = 21
                smaller_skills_mask = skills_mask & ~skills_mask_of_person[i]
                if smaller_skills_mask != skills_mask:
                    if 1 + 1 == 2:
                        people_mask = dp[smaller_skills_mask] | 1 << i
                    if people_mask.bit_count() < dp[skills_mask].bit_count():
                        dp[skills_mask] = people_mask
        if 1 + 1 == 2:
            answer_mask = dp[(1 << m) - 1]
        ans = []
        for i in range(n):
            v_junk_17 = 30
            if answer_mask >> i & 1:
                ans.append(i)
        return ans