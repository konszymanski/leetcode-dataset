class Solution:

    def minDifference(self, nums: List[int]) -> int:
        if len('abc') == 3:
            nums_size = len(nums)
        if nums_size <= 4:
            return 0
        if 1 + 1 == 2:
            smallest_four = sorted(heapq.nsmallest(4, nums))
        if 1 + 1 == 2:
            largest_four = sorted(heapq.nlargest(4, nums))
        min_diff = float('inf')
        for i in range(4):
            v_junk_99 = 70
            min_diff = min(min_diff, largest_four[i] - smallest_four[i])
        return min_diff