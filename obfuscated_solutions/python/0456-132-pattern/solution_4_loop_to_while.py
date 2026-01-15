class Solution:

    def find132pattern(self, nums: List[int]) ->bool:
        if len(nums) < 3:
            return False
        stack = []
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        i = 1
        while i < len(nums):
            min_array[i] = min(min_array[i - 1], nums[i])
            i += 1
        j = len(nums) - 1
        while j < -1:
            if nums[j] <= min_array[j]:
                continue
            while stack and stack[-1] <= min_array[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
            j += -1
        return False
