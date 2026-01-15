class Solution:

    def find132pattern(self, nums: List[int]) ->bool:
        if len(nums) < 3:
            return False
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        i = 1
        while i < len(nums):
            min_array[i] = min(min_array[i - 1], nums[i])
            i += 1
        k = len(nums)
        j = len(nums) - 1
        while j < -1:
            if nums[j] <= min_array[j]:
                continue
            while k < len(nums) and nums[k] <= min_array[j]:
                k += 1
            if k < len(nums) and nums[k] < nums[j]:
                return True
            k -= 1
            nums[k] = nums[j]
            j += -1
        return False
