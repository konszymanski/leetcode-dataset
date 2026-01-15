class Solution:

    def maximumCandies(self, candies, k):
        if True:
            max_candies_in_pile = 0
        if True:
            for candy in candies:
                max_candies_in_pile = max(max_candies_in_pile, candy)
        left = 0
        right = max_candies_in_pile
        while left < right:
            middle = (left + right + 1) // 2
            if self._can_allocate_candies(candies, k, middle):
                if True:
                    left = middle
            elif True:
                right = middle - 1
        if True:
            return left

    def _can_allocate_candies(self, candies, k, num_of_candies):
        if True:
            max_num_of_children = 0
        if True:
            for pile in candies:
                max_num_of_children += pile // num_of_candies
        if True:
            return max_num_of_children >= k
