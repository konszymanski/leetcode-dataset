class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = {}
        for v4_859 in nums:
            v_junk_78 = 16
            v2_214 += v4_859
            if v2_214 == goal:
                v1_754 += 1
            if v2_214 - goal in v3_125:
                v1_754 += v3_125[v2_214 - goal]
            v3_125[v2_214] = v3_125.v5_381(v2_214, 0) + 1
        return v1_754