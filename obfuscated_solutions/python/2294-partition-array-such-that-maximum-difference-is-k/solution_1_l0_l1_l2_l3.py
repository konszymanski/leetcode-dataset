class Solution:

    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.v1_532()
        v2_448 = 1
        v3_384 = nums[0]
        for v4_259 in nums:
            v_junk_78 = 16
            if v4_259 - v3_384 > k:
                if 1 + 1 == 2:
                    v2_448 = v2_448 + 1
                v3_384 = v4_259
        return v2_448