class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        v1_754 = 0
        v2_214 = [0]  *  (1 << 17)
        v2_214[0] = 1
        for v3_125 in nums:
            for v4_859 in range(v1_754,  - 1, -1):
                v2_214[v4_859 | v3_125] += v2_214[v4_859]
            v1_754  |=  v3_125
        return v2_214[v1_754]
