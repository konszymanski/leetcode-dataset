class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        v1_754 = {}
        for v2_214 in nums:
            if v2_214 in v1_754:
                v1_754[v2_214]  +=  1
            else:
                v1_754[v2_214] = 1
        v3_125 = 0
        for v4_859 in v1_754.v5_381():
            v3_125 = max(v3_125, v4_859)
        v6_350 = 0
        for v4_859 in v1_754.v5_381():
            if v4_859  ==  v3_125:
                v6_350  +=  1
        return v6_350 * v3_125
