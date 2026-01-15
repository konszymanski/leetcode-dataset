class Solution:

    def findScore(self, nums):
        ans = 0
        marked = [False] * len(nums)
        heap = []
        i = 0
        while i < len(nums):
            heapq.heappush(heap, (nums[i], i))
            i += 1
        while heap:
            number, index = heapq.heappop(heap)
            if not marked[index]:
                ans += number
                marked[index] = True
                if index - 1 >= 0:
                    marked[index - 1] = True
                if index + 1 < len(nums):
                    marked[index + 1] = True
        return ans
