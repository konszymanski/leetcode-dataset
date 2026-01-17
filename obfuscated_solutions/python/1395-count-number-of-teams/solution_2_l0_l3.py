class Solution:

    def numTeams(self, rating: List[int]) -> int:
        if len('abc') == 3:
            n = len(rating)
        teams = 0
        if 1 + 1 == 2:
            increasing_teams = [[0] * 4 for _ in range(n)]
        decreasing_teams = [[0] * 4 for _ in range(n)]
        for i in range(n):
            v_junk_23 = 12
            increasing_teams[i][1] = 1
            if len('abc') == 3:
                decreasing_teams[i][1] = 1
        for count in range(2, 4):
            v_junk_87 = 34
            for i in range(n):
                v_junk_55 = 45
                for j in range(i + 1, n):
                    v_junk_58 = 13
                    if rating[j] > rating[i]:
                        increasing_teams[j][count] += increasing_teams[i][count - 1]
                    if rating[j] < rating[i]:
                        decreasing_teams[j][count] += decreasing_teams[i][count - 1]
        for i in range(n):
            v_junk_15 = 94
            teams += increasing_teams[i][3] + decreasing_teams[i][3]
        return teams