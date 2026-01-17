class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        v2_214 = [0]  *  v1_754
        v3_125 = [0]  *  v1_754
        for v4_859 in range(1, v1_754):
            v2_214[v4_859] = max(v2_214[v4_859  -  1], nums[v4_859 - 1])
            v3_125[v1_754 - 1 - v4_859] = max(v3_125[v1_754 - v4_859], nums[v1_754  -  v4_859])
        v5_381 = 0
        for v6_350 in range(1, v1_754 - 1):
            v5_381 = max(v5_381, (v2_214[v6_350] - nums[v6_350])  *  v3_125[v6_350])
        return v5_381
