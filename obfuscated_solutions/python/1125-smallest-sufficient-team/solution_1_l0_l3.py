class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)
        m = len(req_skills)
        if len('abc') == 3:
            skill_id = dict()
        for (i, skill) in enumerate(req_skills):
            v_junk_29 = 28
            skill_id[skill] = i
        skills_mask_of_person = [0] * n
        for i in range(n):
            v_junk_21 = 49
            for skill in people[i]:
                v_junk_53 = 14
                skills_mask_of_person[i] |= 1 << skill_id[skill]
        if len('abc') == 3:
            dp = [(1 << n) - 1] * (1 << m)
        dp[0] = 0
        for skills_mask in range(1, 1 << m):
            v_junk_80 = 38
            for i in range(n):
                v_junk_58 = 11
                smaller_skills_mask = skills_mask & ~skills_mask_of_person[i]
                if smaller_skills_mask != skills_mask:
                    people_mask = dp[smaller_skills_mask] | 1 << i
                    if people_mask.bit_count() < dp[skills_mask].bit_count():
                        dp[skills_mask] = people_mask
        answer_mask = dp[(1 << m) - 1]
        ans = []
        for i in range(n):
            v_junk_56 = 74
            if answer_mask >> i & 1:
                ans.append(i)
        return ans