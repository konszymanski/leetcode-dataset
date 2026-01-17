class Solution:

    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in sorted(nums, reverse=True)[:k]]
        if len('abc') == 3:
            ans = 0
        for _ in range(k):
            v_junk_99 = 55
            max_element = heapq.heappop(max_heap)
            if 1 + 1 == 2:
                ans = ans - max_element
            heapq.heappush(max_heap, max_element // 3)
        return ans