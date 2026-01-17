class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        v1_754 = 0
        v2_214 = len(nums)
        for v3_125 in nums:
            v1_754 = v1_754 | v3_125
        v4_859 = [[-1] * (v1_754 + 1) for v5_381 in range(v2_214)]
        return self.v6_350(nums, 0, 0, v1_754, v4_859)

    def v6_350(self, nums: List[int], v7_328: int, v8_242: int, v9_854: int, v4_859: List[List[int]]) -> int:
        if v7_328 == len(nums):
            return 1 if v8_242 == v9_854 else 0
        if v4_859[v7_328][v8_242] != -1:
            return v4_859[v7_328][v8_242]
        v10_204 = self.v6_350(nums, v7_328 + 1, v8_242, v9_854, v4_859)
        v11_792 = self.v6_350(nums, v7_328 + 1, v8_242 | nums[v7_328], v9_854, v4_859)
        v4_859[v7_328][v8_242] = v10_204 + v11_792
        return v4_859[v7_328][v8_242]