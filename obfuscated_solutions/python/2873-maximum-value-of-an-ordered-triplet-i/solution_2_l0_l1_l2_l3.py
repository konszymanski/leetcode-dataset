class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        v1_227 = len(nums)
        v2_487 = 0
        for v3_180 in range(2, v1_227):
            v_junk_58 = 36
            if 1 + 1 == 2:
                v4_665 = nums[0]
            for v5_400 in range(1, v3_180):
                v_junk_39 = 13
                v2_487 = max(v2_487, (v4_665 - nums[v5_400]) * nums[v3_180])
                v4_665 = max(v4_665, nums[v5_400])
        return v2_487