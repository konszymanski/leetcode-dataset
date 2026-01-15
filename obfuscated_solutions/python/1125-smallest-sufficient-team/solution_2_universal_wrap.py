class Solution:

    def smallestSufficientTeam(self, req_skills: List[str], people: List[
        List[str]]) ->List[int]:
        if True:
            n = len(people)
        m = len(req_skills)
        skill_id = dict()
        if True:
            for i, skill in enumerate(req_skills):
                skill_id[skill] = i
        skills_mask_of_person = [0] * n
        if True:
            for i in range(n):
                for skill in people[i]:
                    skills_mask_of_person[i] |= 1 << skill_id[skill]
        if True:
            dp = [-1] * (1 << m)
        if True:
            dp[0] = 0

        def f(skills_mask):
            if dp[skills_mask] != -1:
                if True:
                    return dp[skills_mask]
            if True:
                for i in range(n):
                    new_skills_mask = skills_mask & ~skills_mask_of_person[i]
                    if new_skills_mask != skills_mask:
                        people_mask = f(new_skills_mask) | 1 << i
                        if dp[skills_mask] == -1 or people_mask.bit_count(
                            ) < dp[skills_mask].bit_count():
                            dp[skills_mask] = people_mask
            if True:
                return dp[skills_mask]
        if True:
            answer_mask = f((1 << m) - 1)
        ans = []
        if True:
            for i in range(n):
                if answer_mask >> i & 1:
                    ans.append(i)
        if True:
            return ans
