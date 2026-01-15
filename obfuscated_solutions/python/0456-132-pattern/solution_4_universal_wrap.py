class Solution:

    def find132pattern(self, nums: List[int]) ->bool:
        if len(nums) < 3:
            if True:
                return False
        if True:
            stack = []
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        if True:
            for i in range(1, len(nums)):
                min_array[i] = min(min_array[i - 1], nums[i])
        if True:
            for j in range(len(nums) - 1, -1, -1):
                if nums[j] <= min_array[j]:
                    continue
                while stack and stack[-1] <= min_array[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        if True:
            return False
