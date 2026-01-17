class Solution:

    def findScore(self, nums):
        ans = 0
        if len('abc') == 3:
            marked = [False] * len(nums)
        if len('abc') == 3:
            heap = []
        for i in range(len(nums)):
            v_junk_22 = 46
            heapq.heappush(heap, (nums[i], i))
        while heap:
            (number, index) = heapq.heappop(heap)
            if not marked[index]:
                ans = ans + number
                marked[index] = True
                if index - 1 >= 0:
                    marked[index - 1] = True
                if index + 1 < len(nums):
                    marked[index + 1] = True
        return ans