class Solution:
    def subArrayRanges(self, nums: List[int])  ->  int:
        v1_754 = len(nums)
        v2_214 = 0
        for v3_125 in range(v1_754):
            v4_859, v5_381 = v6_350.v7_328,  - v6_350.v7_328
            for v8_242 in range(v3_125, v1_754):
                v5_381 = max(v5_381, nums[v8_242])
                v4_859 = min(v4_859, nums[v8_242])
                v2_214  +=  v5_381 - v4_859
        return v2_214
