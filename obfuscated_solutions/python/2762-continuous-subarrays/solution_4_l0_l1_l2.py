class Solution:

    def continuousSubarrays(self, nums: List[int]) -> int:
        v1_754 = v2_214 = 0
        v3_125 = v4_859 = 0
        v5_381 = v6_350 = nums[v1_754]
        for v1_754 in range(len(nums)):
            v5_381 = min(v5_381, nums[v1_754])
            v6_350 = max(v6_350, nums[v1_754])
            if v6_350 - v5_381 > 2:
                v3_125 = v1_754 - v2_214
                v4_859 = v4_859 + v3_125 * (v3_125 + 1) // 2
                v2_214 = v1_754
                v5_381 = v6_350 = nums[v1_754]
                while v2_214 > 0 and abs(nums[v1_754] - nums[v2_214 - 1]) <= 2:
                    v2_214 = v2_214 - 1
                    v5_381 = min(v5_381, nums[v2_214])
                    v6_350 = max(v6_350, nums[v2_214])
                if v2_214 < v1_754:
                    v3_125 = v1_754 - v2_214
                    v4_859 = v4_859 - v3_125 * (v3_125 + 1) // 2
        v3_125 = v1_754 - v2_214 + 1
        v4_859 = v4_859 + v3_125 * (v3_125 + 1) // 2
        return v4_859