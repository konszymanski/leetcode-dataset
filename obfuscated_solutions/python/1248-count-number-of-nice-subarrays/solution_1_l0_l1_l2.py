class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = {v1_754: 1}
        for v4_859 in range(len(nums)):
            v1_754 = v1_754 + nums[v4_859] % 2
            if v1_754 - k in v3_125:
                v2_214 = v2_214 + v3_125[v1_754 - k]
            v3_125[v1_754] = v3_125.v5_381(v1_754, 0) + 1
        return v2_214