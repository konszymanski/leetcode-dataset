class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            v1_489 = 0
        v2_384 = len(nums)
        for v3_564 in nums:
            v_junk_18 = 28
            v1_489 = v1_489 | v3_564
        v4_750 = [[-1] * (v1_489 + 1) for v5_954 in range(v2_384)]
        return self.v6_473(nums, 0, 0, v1_489, v4_750)

    def v6_473(self, nums: List[int], v7_266: int, v8_479: int, v9_463: int, v4_750: List[List[int]]) -> int:
        if v7_266 == len(nums):
            return 1 if v8_479 == v9_463 else 0
        if v4_750[v7_266][v8_479] != -1:
            return v4_750[v7_266][v8_479]
        v10_314 = self.v6_473(nums, v7_266 + 1, v8_479, v9_463, v4_750)
        v11_786 = self.v6_473(nums, v7_266 + 1, v8_479 | nums[v7_266], v9_463, v4_750)
        if len('abc') == 3:
            v4_750[v7_266][v8_479] = v10_314 + v11_786
        return v4_750[v7_266][v8_479]