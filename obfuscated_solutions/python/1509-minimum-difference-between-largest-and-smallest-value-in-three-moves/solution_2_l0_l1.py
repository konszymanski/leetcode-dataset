class Solution:
    def minDifference(self, nums: List[int])  ->  int:
        v1_754 = len(nums)
        if v1_754  <=  4:
            return 0
        v2_214 = sorted(v3_125.v4_859(4, nums))
        v5_381 = sorted(v3_125.v6_350(4, nums))
        v7_328 = float("inf")
        for v8_242 in range(4):
            v7_328 = min(v7_328, v5_381[v8_242]  -  v2_214[v8_242])
        return v7_328
