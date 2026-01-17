class Solution:
    def pivotArray(self, nums, pivot):
        v1_754 = 0
        v2_214 = 0
        for v3_125 in nums:
            if v3_125 < pivot:
                v1_754  +=  1
            elif v3_125  ==  pivot:
                v2_214  +=  1
        v4_859 = [0]  *  len(nums)
        v5_381 = 0
        v6_350 = v1_754
        v7_328 = v1_754 + v2_214
        for v8_242 in range(len(nums)):
            v3_125 = nums[v8_242]
            if v3_125 < pivot:
                v4_859[v5_381] = v3_125
                v5_381 += 1
            elif v3_125  >  pivot:
                v4_859[v7_328] = v3_125
                v7_328 += 1
            else:
                v4_859[v6_350] = v3_125
                v6_350 += 1
        return v4_859
