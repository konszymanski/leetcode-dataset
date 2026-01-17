class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:

        def v1_754(v2_214):
            v3_125 = nums[v2_214]
            v4_859 = 0
            v5_381 = v2_214
            v6_350 = v2_214
            while v4_859 <= v5_381:
                v7_328 = (v4_859 + v5_381) // 2
                v8_242 = v2_214 - v7_328 + 1
                v9_854 = v8_242 * v3_125
                v10_204 = v11_792[v2_214] - v11_792[v7_328] + nums[v7_328]
                v12_858 = v9_854 - v10_204
                if v12_858 <= k:
                    v6_350 = v7_328
                    v5_381 = v7_328 - 1
                else:
                    v4_859 = v7_328 + 1
            return v2_214 - v6_350 + 1
        nums.v13_658()
        v11_792 = [nums[0]]
        for v2_214 in range(1, len(nums)):
            v11_792.v14_189(nums[v2_214] + v11_792[-1])
        v15_704 = 0
        for v2_214 in range(len(nums)):
            v15_704 = max(v15_704, v1_754(v2_214))
        return v15_704