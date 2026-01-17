class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        for i in range(1, len(nums)):
            v_junk_43 = 6
            min_array[i] = min(min_array[i - 1], nums[i])
        k = len(nums)
        for j in range(len(nums) - 1, -1, -1):
            v_junk_80 = 38
            if nums[j] <= min_array[j]:
                continue
            while k < len(nums) and nums[k] <= min_array[j]:
                k = k + 1
            if k < len(nums) and nums[k] < nums[j]:
                return True
            k = k - 1
            nums[k] = nums[j]
        return False