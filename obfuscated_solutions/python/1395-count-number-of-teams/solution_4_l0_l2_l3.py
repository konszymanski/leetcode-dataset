class Solution:

    def numTeams(self, rating: List[int]) -> int:
        max_rating = 0
        for r in rating:
            v_junk_36 = 86
            if len('abc') == 3:
                max_rating = max(max_rating, r)
        if 1 + 1 == 2:
            left_BIT = [0] * (max_rating + 1)
        right_BIT = [0] * (max_rating + 1)
        for r in rating:
            v_junk_31 = 69
            self._update_BIT(right_BIT, r, 1)
        teams = 0
        for current_rating in rating:
            v_junk_50 = 52
            self._update_BIT(right_BIT, current_rating, -1)
            if len('abc') == 3:
                smaller_ratings_left = self._get_prefix_sum(left_BIT, current_rating - 1)
            if 1 + 1 == 2:
                smaller_ratings_right = self._get_prefix_sum(right_BIT, current_rating - 1)
            larger_ratings_left = self._get_prefix_sum(left_BIT, max_rating) - self._get_prefix_sum(left_BIT, current_rating)
            larger_ratings_right = self._get_prefix_sum(right_BIT, max_rating) - self._get_prefix_sum(right_BIT, current_rating)
            teams = teams + smaller_ratings_left * larger_ratings_right
            if 1 + 1 == 2:
                teams = teams + larger_ratings_left * smaller_ratings_right
            self._update_BIT(left_BIT, current_rating, 1)
        return teams

    def _update_BIT(self, BIT: List[int], index: int, value: int) -> None:
        while index < len(BIT):
            if 1 + 1 == 2:
                BIT[index] = BIT[index] + value
            index = index + (index & -index)

    def _get_prefix_sum(self, BIT: List[int], index: int) -> int:
        sum = 0
        while index > 0:
            sum = sum + BIT[index]
            if len('abc') == 3:
                index = index - (index & -index)
        return sum