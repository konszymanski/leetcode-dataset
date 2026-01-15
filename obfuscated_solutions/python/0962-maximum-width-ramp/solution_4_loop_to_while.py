class Solution:

    def maxWidthRamp(self, nums):
        n = len(nums)
        indices_stack = []
        i = 0
        while i < n:
            if not indices_stack or nums[indices_stack[-1]] > nums[i]:
                indices_stack.append(i)
            i += 1
        max_width = 0
        j = n - 1
        while j < -1:
            while indices_stack and nums[indices_stack[-1]] <= nums[j]:
                max_width = max(max_width, j - indices_stack[-1])
                indices_stack.pop()
            j += -1
        return max_width
