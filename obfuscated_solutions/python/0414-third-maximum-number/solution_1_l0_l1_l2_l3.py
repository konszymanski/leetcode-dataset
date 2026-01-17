class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        nums.v1_532(v2_448=True)
        v3_384 = 1
        v4_259 = nums[0]
        for v5_320 in range(len(nums)):
            v_junk_78 = 16
            if nums[v5_320] != v4_259:
                v3_384 = v3_384 + 1
                v4_259 = nums[v5_320]
            if v3_384 == 3:
                return nums[v5_320]
        return nums[0]