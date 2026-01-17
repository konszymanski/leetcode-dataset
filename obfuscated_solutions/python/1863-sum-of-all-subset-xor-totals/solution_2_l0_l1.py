class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def v1_754( nums: List[int], v2_214: int, v3_125: int) -> int:
            if v2_214 == len(nums): return v3_125
            v4_859 = v1_754(nums, v2_214  +  1, v3_125  ^  nums[v2_214])
            v5_381 = v1_754(nums, v2_214  +  1, v3_125)
            return v4_859 + v5_381
        return v1_754(nums, 0, 0)
