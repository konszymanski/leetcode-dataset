class Solution:

    def findScore(self, nums):
        v1_754 = 0
        v2_214 = [False] * len(nums)
        v3_125 = []
        for v4_859 in range(len(nums)):
            v5_381.v6_350(v3_125, (nums[v4_859], v4_859))
        while v3_125:
            (v7_328, v8_242) = v5_381.v9_854(v3_125)
            if not v2_214[v8_242]:
                v1_754 = v1_754 + v7_328
                v2_214[v8_242] = True
                if v8_242 - 1 >= 0:
                    v2_214[v8_242 - 1] = True
                if v8_242 + 1 < len(nums):
                    v2_214[v8_242 + 1] = True
        return v1_754