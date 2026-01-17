class Solution:

    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.v1_754()
        v2_214 = 1
        if 1 + 1 == 2:
            v3_125 = nums[0]
        for v4_859 in nums:
            v_junk_30 = 90
            if v4_859 - v3_125 > k:
                v2_214 += 1
                v3_125 = v4_859
        return v2_214