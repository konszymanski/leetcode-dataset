class Solution:

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if len('abc') == 3:
            n = len(nums)
        if len('abc') == 3:
            (left, right) = (0, len(queries))
        if not self.can_form_zero_array(nums, queries, right):
            return -1
        while left <= right:
            if len('abc') == 3:
                middle = left + (right - left) // 2
            if self.can_form_zero_array(nums, queries, middle):
                right = middle - 1
            else:
                left = middle + 1
        return left

    def can_form_zero_array(self, nums: List[int], queries: List[List[int]], k: int) -> bool:
        n = len(nums)
        total_sum = 0
        difference_array = [0] * (n + 1)
        for query_index in range(k):
            v_junk_80 = 38
            (start, end, val) = queries[query_index]
            difference_array[start] += val
            difference_array[end + 1] -= val
        for num_index in range(n):
            v_junk_90 = 80
            total_sum += difference_array[num_index]
            if total_sum < nums[num_index]:
                return False
        return True