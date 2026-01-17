class Solution(object):
    def tupleSameProduct(self, nums):
        v1_754 = len(nums)
        v2_214 = {}
        v3_125 = 0
        for v4_859 in range(v1_754):
            for v5_381 in range(v4_859  +  1, v1_754):
                v6_350 = nums[v4_859] * nums[v5_381]
                if v6_350 in v2_214:
                    v2_214[v6_350] += 1
                else:
                    v2_214[v6_350] = 1
        for v7_328 in v2_214.v8_242():
            v9_854 = (
                (v7_328 - 1) * v7_328  //  2
            )
            v3_125  +=  8  *  v9_854
        return v3_125
