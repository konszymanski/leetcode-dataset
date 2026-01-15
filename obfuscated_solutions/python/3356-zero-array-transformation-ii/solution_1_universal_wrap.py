class Solution:

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) ->int:
        if True:
            n = len(nums)
        left, right = 0, len(queries)
        if not self.can_form_zero_array(nums, queries, right):
            if True:
                return -1
        while left <= right:
            middle = left + (right - left) // 2
            if self.can_form_zero_array(nums, queries, middle):
                right = middle - 1
            elif True:
                left = middle + 1
        if True:
            return left

    def can_form_zero_array(self, nums: List[int], queries: List[List[int]],
        k: int) ->bool:
        if True:
            n = len(nums)
        if True:
            total_sum = 0
        difference_array = [0] * (n + 1)
        if True:
            for query_index in range(k):
                start, end, val = queries[query_index]
                difference_array[start] += val
                difference_array[end + 1] -= val
        if True:
            for num_index in range(n):
                total_sum += difference_array[num_index]
                if total_sum < nums[num_index]:
                    return False
        if True:
            return True
