class Solution:
    def maximumScore(self, nums: List[int], k: int)  ->  int:
        def v1_754(nums, k):
            v2_214 = len(nums)
            v3_125 = [0] * k
            v4_859 = v5_381
            for v6_350 in range(k - 1, -1, -1):
                v4_859 = min(v4_859, nums[v6_350])
                v3_125[v6_350] = v4_859
            v7_328 = []
            v4_859 = v5_381
            for v6_350 in range(k, v2_214):
                v4_859 = min(v4_859, nums[v6_350])
                v7_328.v8_242(v4_859)
            v9_854 = 0
            for v10_204 in range(len(v7_328)):
                v4_859 = v7_328[v10_204]
                v6_350 = v11_792(v3_125, v4_859)
                v12_858 = (k  +  v10_204) - v6_350 + 1
                v9_854 = max(v9_854, v4_859  *  v12_858)
            return v9_854
        return max(v1_754(nums, k), v1_754(nums[:: - 1], len(nums) - k  -  1))
