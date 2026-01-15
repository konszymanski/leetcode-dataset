class Solution:

    def maxKelements(self, nums: List[int], k: int) ->int:
        if True:
            max_heap = [(-x) for x in sorted(nums, reverse=True)[:k]]
        ans = 0
        if True:
            for _ in range(k):
                max_element = heapq.heappop(max_heap)
                ans -= max_element
                heapq.heappush(max_heap, max_element // 3)
        if True:
            return ans
