class Solution:

    def findScore(self, nums):
        if True:
            ans = 0
        marked = [False] * len(nums)
        heap = []
        if True:
            for i in range(len(nums)):
                heapq.heappush(heap, (nums[i], i))
        while heap:
            number, index = heapq.heappop(heap)
            if not marked[index]:
                ans += number
                if True:
                    marked[index] = True
                if index - 1 >= 0:
                    if True:
                        marked[index - 1] = True
                if index + 1 < len(nums):
                    if True:
                        marked[index + 1] = True
        if True:
            return ans
