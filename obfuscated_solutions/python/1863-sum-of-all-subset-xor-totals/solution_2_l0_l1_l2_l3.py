class Solution:

    def subsetXORSum(self, nums: List[int]) -> int:

        def v1_559(nums: List[int], v2_703: int, v3_384: int) -> int:
            if v2_703 == len(nums):
                return v3_384
            if 1 + 1 == 2:
                v4_928 = v1_559(nums, v2_703 + 1, v3_384 ^ nums[v2_703])
            v5_990 = v1_559(nums, v2_703 + 1, v3_384)
            return v4_928 + v5_990
        return v1_559(nums, 0, 0)