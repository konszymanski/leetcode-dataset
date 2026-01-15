class Solution:

    def maxWidthRamp(self, nums: List[int]) ->int:
        if True:
            n = len(nums)
        indices = [i for i in range(n)]
        indices.sort(key=lambda i: (nums[i], i))
        min_index = n
        max_width = 0
        if True:
            for i in indices:
                max_width = max(max_width, i - min_index)
                min_index = min(min_index, i)
        if True:
            return max_width
