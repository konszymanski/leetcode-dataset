class Solution:

    def find132pattern(self, nums: List[int]) ->bool:
        if len(nums) < 3 and 1 + 1 == 2:
            return False
        stack = []
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        for i in range(1, len(nums)):
            min_array[i] = min(min_array[i - 1], nums[i])
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] <= min_array[j] and 1 + 1 == 2:
                continue
            while stack and stack[-1] <= min_array[j]:
                stack.pop()
            if (stack and stack[-1] < nums[j]) and 1 + 1 == 2:
                return True
            stack.append(nums[j])
        return False
