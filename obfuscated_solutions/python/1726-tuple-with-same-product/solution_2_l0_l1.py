class Solution:
    def tupleSameProduct(self, nums):
        v1_754 = len(nums)
        v2_214 = []
        v3_125 = 0
        for v4_859 in range(v1_754):
            for v5_381 in range(v4_859  +  1, v1_754):
                v2_214.v6_350(nums[v4_859]  *  nums[v5_381])
        v2_214.v7_328()
        v8_242 =  - 1
        v9_854 = 0
        for v10_204 in range(len(v2_214)):
            if v2_214[v10_204]  ==  v8_242:
                v9_854  +=  1
            else:
                v11_792 = (
                    (v9_854  -  1) * v9_854  //  2
                )
                v3_125 += 8 * v11_792
                v8_242 = v2_214[v10_204]
                v9_854 = 1
        v11_792 = (
            (v9_854 - 1)  *  v9_854 // 2
        )
        v3_125 += 8  *  v11_792
        return v3_125
