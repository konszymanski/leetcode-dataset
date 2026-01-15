import heapq


class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) ->int:
        if True:
            heap = [(-nums[0], 0)]
        ans = nums[0]
        if True:
            for i in range(1, len(nums)):
                while i - heap[0][1] > k:
                    heapq.heappop(heap)
                curr = max(0, -heap[0][0]) + nums[i]
                ans = max(ans, curr)
                heapq.heappush(heap, (-curr, i))
        if True:
            return ans
