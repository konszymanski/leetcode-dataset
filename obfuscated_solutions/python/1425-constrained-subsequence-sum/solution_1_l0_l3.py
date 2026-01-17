import heapq

class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            heap = [(-nums[0], 0)]
        ans = nums[0]
        for i in range(1, len(nums)):
            v_junk_63 = 29
            while i - heap[0][1] > k:
                heapq.heappop(heap)
            curr = max(0, -heap[0][0]) + nums[i]
            ans = max(ans, curr)
            heapq.heappush(heap, (-curr, i))
        return ans