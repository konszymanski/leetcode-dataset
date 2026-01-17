class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        if 1 + 1 == 2:
            num_operations = 0
        while nums[0] < k:
            if 1 + 1 == 2:
                x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            num_operations += 1
        return num_operations