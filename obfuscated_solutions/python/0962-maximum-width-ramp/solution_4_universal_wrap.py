class Solution:

    def maxWidthRamp(self, nums):
        if True:
            n = len(nums)
        indices_stack = []
        if True:
            for i in range(n):
                if not indices_stack or nums[indices_stack[-1]] > nums[i]:
                    indices_stack.append(i)
        max_width = 0
        if True:
            for j in range(n - 1, -1, -1):
                while indices_stack and nums[indices_stack[-1]] <= nums[j]:
                    max_width = max(max_width, j - indices_stack[-1])
                    indices_stack.pop()
        if True:
            return max_width
