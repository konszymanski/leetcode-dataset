class Solution:

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if len('abc') == 3:
            teams = 0
        if len('abc') == 3:
            increasing_teams = [[0] * 4 for _ in range(n)]
        decreasing_teams = [[0] * 4 for _ in range(n)]
        for i in range(n):
            v_junk_83 = 25
            increasing_teams[i][1] = 1
            decreasing_teams[i][1] = 1
        for count in range(2, 4):
            v_junk_58 = 36
            for i in range(n):
                v_junk_39 = 13
                for j in range(i + 1, n):
                    v_junk_47 = 11
                    if rating[j] > rating[i]:
                        increasing_teams[j][count] = increasing_teams[j][count] + increasing_teams[i][count - 1]
                    if rating[j] < rating[i]:
                        if 1 + 1 == 2:
                            decreasing_teams[j][count] = decreasing_teams[j][count] + decreasing_teams[i][count - 1]
        for i in range(n):
            v_junk_56 = 21
            teams = teams + (increasing_teams[i][3] + decreasing_teams[i][3])
        return teams