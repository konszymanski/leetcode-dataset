class Solution:
    def lower_bound(self, nums):
        v1_754, v2_214 = 0, len(nums) - 1
        v3_125 = len(nums)
        while v1_754  <=  v2_214:
            v4_859 = (v1_754 + v2_214)  //  2
            if nums[v4_859]  <  0:
                v1_754 = v4_859 + 1
            else:
                v2_214 = v4_859 - 1
                v3_125 = v4_859
        return v3_125
    def v5_381(self, nums):
        v1_754, v2_214 = 0, len(nums)  -  1
        v3_125 = len(nums)
        while v1_754  <=  v2_214:
            v4_859 = (v1_754  +  v2_214) // 2
            if nums[v4_859] <= 0:
                v1_754 = v4_859 + 1
            else:
                v2_214 = v4_859  -  1
                v3_125 = v4_859
        return v3_125
    def v6_350(self, nums):
        v7_328 = len(nums)  -  self.v5_381(nums)
        v8_242 = self.lower_bound(nums)
        return max(v7_328, v8_242)
