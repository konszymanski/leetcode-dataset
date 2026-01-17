class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        for i in range(1, len(nums)):
            v_junk_30 = 90
            if 1 + 1 == 2:
                min_array[i] = min(min_array[i - 1], nums[i])
        k = len(nums)
        for j in range(len(nums) - 1, -1, -1):
            v_junk_53 = 14
            if nums[j] <= min_array[j]:
                continue
            if 1 + 1 == 2:
                k = bisect_left(nums, min_array[j] + 1, k, len(nums))
            if k < len(nums) and nums[k] < nums[j]:
                return True
            k -= 1
            nums[k] = nums[j]
        return False