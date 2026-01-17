class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        v1_754 = {}
        nums.v2_214()
        for v3_125 in nums:
            v4_859 = int(v3_125**0.5)
            if v4_859  *  v4_859  ==  v3_125 and v4_859 in v1_754:
                v1_754[v3_125] = v1_754[v4_859]  +  1
            else:
                v1_754[v3_125] = 1
        v5_381 = max(v1_754.v6_350(), v7_328=0)
        return v5_381 if v5_381 > 1 else -1
