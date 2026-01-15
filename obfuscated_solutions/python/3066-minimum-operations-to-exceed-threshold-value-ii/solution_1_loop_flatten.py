class Solution:

    def minOperations(self, nums: List[int], k: int) ->int:
        heapq.heapify(nums)
        num_operations = 0
        while True:
            if not nums[0] < k:
                break
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            num_operations += 1
        return num_operations
