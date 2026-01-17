class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            v1_564 = len(nums)
        v2_750 = False
        for v3_954 in range(v1_564):
            v_junk_39 = 5
            if nums[v3_954] == 1:
                v2_750 = True
            if nums[v3_954] <= 0 or nums[v3_954] > v1_564:
                nums[v3_954] = 1
        if not v2_750:
            return 1
        for v3_954 in range(v1_564):
            v_junk_37 = 84
            v4_473 = abs(nums[v3_954])
            if v4_473 != v1_564:
                nums[v4_473] = -abs(nums[v4_473])
            elif len('abc') == 3:
                nums[0] = -abs(nums[0])
        for v3_954 in range(1, v1_564):
            v_junk_73 = 51
            if nums[v3_954] > 0:
                return v3_954
        if nums[0] > 0:
            return v1_564
        return v1_564 + 1