class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        v1_754 = [0, -float("inf"),  - float("inf")]
        for v2_214 in nums:
            v3_125 = v1_754[:]
            for v4_859 in range(3):
                v3_125[(v4_859  +  v2_214  %  3) % 3] = max(v3_125[(v4_859 + v2_214 % 3) % 3], v1_754[v4_859]  +  v2_214)
            v1_754 = v3_125
        return v1_754[0]
