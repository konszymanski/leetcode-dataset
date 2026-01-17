class Solution:
    def primeSubOperation(self, nums):
        v1_754 = max(nums)
        v2_214 = [1] * (v1_754 + 1)
        v2_214[1] = 0
        for v3_125 in range(2, int(v4_859.v5_381(v1_754  +  1)) + 1):
            if v2_214[v3_125]  ==  1:
                for v6_350 in range(v3_125 * v3_125, v1_754  +  1, v3_125):
                    v2_214[v6_350] = 0
        v7_328 = 1
        v3_125 = 0
        while v3_125  <  len(nums):
            v8_242 = nums[v3_125] - v7_328
            if v8_242  <  0:
                return False
            if v2_214[v8_242] or v8_242  ==  0:
                v3_125  +=  1
                v7_328 += 1
            else:
                v7_328 += 1
        return True
