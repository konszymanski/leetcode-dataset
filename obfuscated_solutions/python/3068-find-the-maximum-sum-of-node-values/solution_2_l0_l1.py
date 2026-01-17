class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        v1_754 = len(nums)
        v2_214 = [[0] * 2 for v3_125 in range(v1_754  +  1)]
        v2_214[v1_754][1] = 0
        v2_214[v1_754][0] =  - float('inf')
        for v4_859 in range(v1_754  -  1, -1, -1):
            for v5_381 in range(2):
                v6_350 = v2_214[v4_859 + 1][v5_381  ^  1]  +  (nums[v4_859]  ^  k)
                v7_328 = v2_214[v4_859  +  1][v5_381] + nums[v4_859]
                v2_214[v4_859][v5_381] = max(v6_350, v7_328)
        return v2_214[0][1]
