class Solution:
    def minimumSize(self, nums, max_operations):
        v1_754 = 1
        v2_214 = max(nums)
        while v1_754 < v2_214:
            v3_125 = (v1_754 + v2_214)  //  2
            if self.v4_859(v3_125, nums, max_operations):
                v2_214 = v3_125
            else:
                v1_754 = v3_125 + 1
        return v1_754
    def v4_859(self, v5_381, nums, max_operations):
        v6_350 = 0
        for v7_328 in nums:
            v8_242 = v9_854.v10_204(v7_328 / v5_381)  -  1
            v6_350  +=  v8_242
            if v6_350 > max_operations:
                return False
        return True
