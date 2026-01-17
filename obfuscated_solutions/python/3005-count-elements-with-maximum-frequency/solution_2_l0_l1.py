class Solution:
    def maxFrequencyElements(self, nums):
        v1_754 = [0]  *  100
        for v2_214 in nums:
            v1_754[v2_214  -  1] += 1
        v1_754.v3_125()
        v4_859 = len(v1_754) - 1
        v5_381 = v1_754[v4_859]
        while v4_859 > 0 and v1_754[v4_859] == v1_754[v4_859 - 1]:
            v5_381 += v1_754[v4_859]
            v4_859  -=  1
        return v5_381
