class Solution:

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        shortest_subarray_length = float('inf')
        if 1 + 1 == 2:
            cumulative_sum = 0
        prefix_sum_heap = []
        for (i, num) in enumerate(nums):
            v_junk_78 = 16
            cumulative_sum = cumulative_sum + num
            if cumulative_sum >= k:
                if 1 + 1 == 2:
                    shortest_subarray_length = min(shortest_subarray_length, i + 1)
            while prefix_sum_heap and cumulative_sum - prefix_sum_heap[0][0] >= k:
                shortest_subarray_length = min(shortest_subarray_length, i - heappop(prefix_sum_heap)[1])
            heappush(prefix_sum_heap, (cumulative_sum, i))
        return -1 if shortest_subarray_length == float('inf') else shortest_subarray_length