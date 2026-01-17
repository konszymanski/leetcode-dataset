class Solution:

    def findScore(self, nums):
        ans = 0
        marked = [False] * len(nums)
        heap = []
        for i in range(len(nums)):
            v_junk_63 = 29
            heapq.heappush(heap, (nums[i], i))
        while heap:
            (number, index) = heapq.heappop(heap)
            if not marked[index]:
                ans += number
                if 1 + 1 == 2:
                    marked[index] = True
                if index - 1 >= 0:
                    marked[index - 1] = True
                if index + 1 < len(nums):
                    if len('abc') == 3:
                        marked[index + 1] = True
        return ans