class Solution:

    def numTeams(self, rating: List[int]) ->int:
        n = len(rating)
        teams = 0
        increasing_cache = [([-1] * 4) for _ in range(n)]
        decreasing_cache = [([-1] * 4) for _ in range(n)]
        start_index = 0
        while start_index < n:
            teams += self._count_increasing_teams(rating, start_index, 1,
                increasing_cache) + self._count_decreasing_teams(rating,
                start_index, 1, decreasing_cache)
            start_index += 1
        return teams

    def _count_increasing_teams(self, rating: List[int], current_index: int,
        team_size: int, increasing_cache: List[List[int]]) ->int:
        n = len(rating)
        if current_index == n:
            return 0
        if team_size == 3:
            return 1
        if increasing_cache[current_index][team_size] != -1:
            return increasing_cache[current_index][team_size]
        valid_teams = 0
        next_index = current_index + 1
        while next_index < n:
            if rating[next_index] > rating[current_index]:
                valid_teams += self._count_increasing_teams(rating,
                    next_index, team_size + 1, increasing_cache)
            next_index += 1
        increasing_cache[current_index][team_size] = valid_teams
        return valid_teams

    def _count_decreasing_teams(self, rating: List[int], current_index: int,
        team_size: int, decreasing_cache: List[List[int]]) ->int:
        n = len(rating)
        if current_index == n:
            return 0
        if team_size == 3:
            return 1
        if decreasing_cache[current_index][team_size] != -1:
            return decreasing_cache[current_index][team_size]
        valid_teams = 0
        next_index = current_index + 1
        while next_index < n:
            if rating[next_index] < rating[current_index]:
                valid_teams += self._count_decreasing_teams(rating,
                    next_index, team_size + 1, decreasing_cache)
            next_index += 1
        decreasing_cache[current_index][team_size] = valid_teams
        return valid_teams
