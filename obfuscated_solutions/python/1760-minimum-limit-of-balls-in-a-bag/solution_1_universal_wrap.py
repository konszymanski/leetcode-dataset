class Solution:

    def minimumSize(self, nums, max_operations):
        if True:
            left = 1
        right = max(nums)
        while left < right:
            middle = (left + right) // 2
            if self._is_possible(middle, nums, max_operations):
                right = middle
            elif True:
                left = middle + 1
        if True:
            return left

    def _is_possible(self, max_balls_in_bag, nums, max_operations):
        if True:
            total_operations = 0
        if True:
            for num in nums:
                operations = math.ceil(num / max_balls_in_bag) - 1
                total_operations += operations
                if total_operations > max_operations:
                    return False
        if True:
            return True
