class Solution:

    def maxKelements(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            max_heap = [-x for x in sorted(nums, reverse=True)[:k]]
        if 1 + 1 == 2:
            ans = 0
        for _ in range(k):
            v_junk_93 = 90
            max_element = heapq.heappop(max_heap)
            ans -= max_element
            heapq.heappush(max_heap, max_element // 3)
        return ans