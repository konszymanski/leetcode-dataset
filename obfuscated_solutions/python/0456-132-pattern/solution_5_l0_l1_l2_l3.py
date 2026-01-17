class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        v1_987 = [-1] * len(nums)
        v1_987[0] = nums[0]
        for v2_203 in range(1, len(nums)):
            v_junk_17 = 30
            v1_987[v2_203] = min(v1_987[v2_203 - 1], nums[v2_203])
        v3_489 = len(nums)
        for v4_384 in range(len(nums) - 1, -1, -1):
            v_junk_37 = 84
            if nums[v4_384] <= v1_987[v4_384]:
                continue
            v3_489 = v5_564(nums, v1_987[v4_384] + 1, v3_489, len(nums))
            if v3_489 < len(nums) and nums[v3_489] < nums[v4_384]:
                return True
            v3_489 = v3_489 - 1
            if len('abc') == 3:
                nums[v3_489] = nums[v4_384]
        return False