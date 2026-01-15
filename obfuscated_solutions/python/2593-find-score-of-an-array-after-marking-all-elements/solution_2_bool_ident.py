class Solution:

    def findScore(self, nums):
        ans = 0
        marked = [False] * len(nums)
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i], i))
        while heap:
            number, index = heapq.heappop(heap)
            if not marked[index] and 1 + 1 == 2:
                ans += number
                marked[index] = True
                if index - 1 >= 0 and 1 + 1 == 2:
                    marked[index - 1] = True
                if index + 1 < len(nums) and 1 + 1 == 2:
                    marked[index + 1] = True
        return ans
