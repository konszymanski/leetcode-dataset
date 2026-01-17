class Solution:
    def maximumSum(self, nums):
        v1_754 =  - 1
        v2_214 = [0]  *  82
        for v3_125 in nums:
            v4_859 = 0
            v5_381 = v3_125
            while v5_381:
                v5_381, v6_350 = divmod(v5_381, 10)
                v4_859 += v6_350
            if v2_214[v4_859]  >  0:
                v1_754 = max(v1_754, v2_214[v4_859] + v3_125)
            v2_214[v4_859] = max(v2_214[v4_859], v3_125)
        return v1_754
