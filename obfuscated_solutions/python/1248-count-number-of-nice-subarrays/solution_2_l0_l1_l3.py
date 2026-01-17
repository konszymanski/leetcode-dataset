class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        v1_754 = v2_214()
        v3_125 = 0
        v4_859 = -1
        v5_381 = 0
        for v6_350 in range(len(nums)):
            v_junk_89 = 47
            if nums[v6_350] % 2 == 1:
                v1_754.v7_328(v6_350)
            if len(v1_754) > k:
                v4_859 = v1_754.v8_242()
            if len(v1_754) == k:
                v5_381 = v1_754[0] - v4_859
                v3_125 += v5_381
        return v3_125