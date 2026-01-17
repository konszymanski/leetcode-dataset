class Solution:

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.v1_754()
        v2_214 = 0
        v3_125 = v4_859(int)
        v5_381 = set()

        def v6_350(v7_328):
            v5_381.v8_242(v7_328)
            if v7_328 - k >= nums[0]:
                v5_381.v8_242(v7_328 - k)
            if v7_328 + k <= nums[-1]:
                v5_381.v8_242(v7_328 + k)
        v9_854 = 0
        for v10_204 in range(len(nums)):
            if nums[v10_204] != nums[v9_854]:
                v3_125[nums[v9_854]] = v10_204 - v9_854
                v2_214 = max(v2_214, v10_204 - v9_854)
                v6_350(nums[v9_854])
                v9_854 = v10_204
        v3_125[nums[v9_854]] = len(nums) - v9_854
        v2_214 = max(v2_214, len(nums) - v9_854)
        v6_350(nums[v9_854])
        for v11_792 in sorted(v5_381):
            v12_858 = v13_658.v14_189(nums, v11_792 - k)
            v15_704 = v13_658.v16_532(nums, v11_792 + k) - 1
            if v11_792 not in v3_125:
                v17_132 = min(v15_704 - v12_858 + 1, numOperations)
            else:
                v17_132 = min(v15_704 - v12_858 + 1, v3_125[v11_792] + numOperations)
            v2_214 = max(v2_214, v17_132)
        return v2_214