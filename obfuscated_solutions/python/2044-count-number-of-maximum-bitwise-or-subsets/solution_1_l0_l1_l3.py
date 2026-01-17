class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_754 = 0
        for v2_214 in nums:
            v_junk_87 = 34
            v1_754 |= v2_214
        return self.v3_125(nums, 0, 0, v1_754)

    def v3_125(self, nums: List[int], v4_859: int, v5_381: int, v6_350: int) -> int:
        if v4_859 == len(nums):
            return 1 if v5_381 == v6_350 else 0
        v7_328 = self.v3_125(nums, v4_859 + 1, v5_381, v6_350)
        v8_242 = self.v3_125(nums, v4_859 + 1, v5_381 | nums[v4_859], v6_350)
        return v7_328 + v8_242