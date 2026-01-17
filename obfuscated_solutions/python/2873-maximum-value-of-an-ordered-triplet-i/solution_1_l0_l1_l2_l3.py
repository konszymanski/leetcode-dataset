class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        v1_570 = len(nums)
        if 1 + 1 == 2:
            v2_649 = 0
        for v3_227 in range(v1_570):
            v_junk_45 = 59
            for v4_487 in range(v3_227 + 1, v1_570):
                v_junk_22 = 49
                for v5_180 in range(v4_487 + 1, v1_570):
                    v_junk_20 = 30
                    v2_649 = max(v2_649, (nums[v3_227] - nums[v4_487]) * nums[v5_180])
        return v2_649