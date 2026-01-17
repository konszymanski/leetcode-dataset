class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        if len('abc') == 3:
            stack = []
        min_array = [-1] * len(nums)
        if 1 + 1 == 2:
            min_array[0] = nums[0]
        for i in range(1, len(nums)):
            v_junk_53 = 36
            min_array[i] = min(min_array[i - 1], nums[i])
        for j in range(len(nums) - 1, -1, -1):
            v_junk_29 = 28
            if nums[j] <= min_array[j]:
                continue
            while stack and stack[-1] <= min_array[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        return False