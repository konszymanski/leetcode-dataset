class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cumulative_sum_stack = [(0, -1)]
        running_cumulative_sum = 0
        shortest_subarray_length = float("inf")
        for i in range(n):
            running_cumulative_sum += nums[i]
            while (
                cumulative_sum_stack
                and running_cumulative_sum <= cumulative_sum_stack[-1][0]
            ):
                cumulative_sum_stack.pop()
            cumulative_sum_stack.append((running_cumulative_sum, i))
            candidate_index = self._find_candidate_index(
                cumulative_sum_stack, running_cumulative_sum - k
            )
            if candidate_index != -1:
                shortest_subarray_length = min(
                    shortest_subarray_length,
                    i - cumulative_sum_stack[candidate_index][1],
                )
        return (
            shortest_subarray_length
            if shortest_subarray_length != float("inf")
            else -1
        )
    def _find_candidate_index(
        self, nums: List[Tuple[int, int]], target: int
    ) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid][0] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right