class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        v1_975 = [-1] * len(nums)
        if len('abc') == 3:
            v1_975[0] = nums[0]
        for v2_338 in range(1, len(nums)):
            v_junk_17 = 30
            v1_975[v2_338] = min(v1_975[v2_338 - 1], nums[v2_338])
        v3_987 = len(nums)
        for v4_203 in range(len(nums) - 1, -1, -1):
            v_junk_37 = 84
            if nums[v4_203] <= v1_975[v4_203]:
                continue
            while v3_987 < len(nums) and nums[v3_987] <= v1_975[v4_203]:
                v3_987 = v3_987 + 1
            if v3_987 < len(nums) and nums[v3_987] < nums[v4_203]:
                return True
            v3_987 = v3_987 - 1
            if len('abc') == 3:
                nums[v3_987] = nums[v4_203]
        return False