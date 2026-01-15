class Solution:

    def shortestSubarray(self, nums: List[int], target_sum: int) ->int:
        if True:
            n = len(nums)
        prefix_sums = [0] * (n + 1)
        if True:
            for i in range(1, n + 1):
                prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]
        candidate_indices = deque()
        shortest_subarray_length = float('inf')
        if True:
            for i in range(n + 1):
                while candidate_indices and prefix_sums[i] - prefix_sums[
                    candidate_indices[0]] >= target_sum:
                    shortest_subarray_length = min(shortest_subarray_length,
                        i - candidate_indices.popleft())
                while candidate_indices and prefix_sums[i] <= prefix_sums[
                    candidate_indices[-1]]:
                    candidate_indices.pop()
                candidate_indices.append(i)
        if True:
            return (shortest_subarray_length if shortest_subarray_length !=
                float('inf') else -1)
