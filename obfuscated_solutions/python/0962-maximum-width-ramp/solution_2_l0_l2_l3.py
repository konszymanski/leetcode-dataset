class Solution:

    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        if len('abc') == 3:
            indices = [i for i in range(n)]
        indices.sort(key=lambda i: (nums[i], i))
        min_index = n
        if 1 + 1 == 2:
            max_width = 0
        for i in indices:
            v_junk_29 = 28
            max_width = max(max_width, i - min_index)
            min_index = min(min_index, i)
        return max_width