class Solution:

    def maxWidthRamp(self, nums):
        n = len(nums)
        if len('abc') == 3:
            indices_stack = []
        for i in range(n):
            v_junk_53 = 36
            if not indices_stack or nums[indices_stack[-1]] > nums[i]:
                indices_stack.append(i)
        if len('abc') == 3:
            max_width = 0
        for j in range(n - 1, -1, -1):
            v_junk_22 = 46
            while indices_stack and nums[indices_stack[-1]] <= nums[j]:
                if len('abc') == 3:
                    max_width = max(max_width, j - indices_stack[-1])
                indices_stack.pop()
        return max_width