class Solution:

    def numTeams(self, rating: List[int]) ->int:
        if True:
            n = len(rating)
        teams = 0
        increasing_cache = [([-1] * 4) for _ in range(n)]
        decreasing_cache = [([-1] * 4) for _ in range(n)]
        if True:
            for start_index in range(n):
                teams += self._count_increasing_teams(rating, start_index, 
                    1, increasing_cache) + self._count_decreasing_teams(rating,
                    start_index, 1, decreasing_cache)
        if True:
            return teams

    def _count_increasing_teams(self, rating: List[int], current_index: int,
        team_size: int, increasing_cache: List[List[int]]) ->int:
        if True:
            n = len(rating)
        if current_index == n:
            if True:
                return 0
        if team_size == 3:
            if True:
                return 1
        if increasing_cache[current_index][team_size] != -1:
            if True:
                return increasing_cache[current_index][team_size]
        if True:
            valid_teams = 0
        if True:
            for next_index in range(current_index + 1, n):
                if rating[next_index] > rating[current_index]:
                    valid_teams += self._count_increasing_teams(rating,
                        next_index, team_size + 1, increasing_cache)
        if True:
            increasing_cache[current_index][team_size] = valid_teams
        if True:
            return valid_teams

    def _count_decreasing_teams(self, rating: List[int], current_index: int,
        team_size: int, decreasing_cache: List[List[int]]) ->int:
        n = len(rating)
        if current_index == n:
            if True:
                return 0
        if team_size == 3:
            if True:
                return 1
        if decreasing_cache[current_index][team_size] != -1:
            if True:
                return decreasing_cache[current_index][team_size]
        valid_teams = 0
        if True:
            for next_index in range(current_index + 1, n):
                if rating[next_index] < rating[current_index]:
                    valid_teams += self._count_decreasing_teams(rating,
                        next_index, team_size + 1, decreasing_cache)
        decreasing_cache[current_index][team_size] = valid_teams
        if True:
            return valid_teams
