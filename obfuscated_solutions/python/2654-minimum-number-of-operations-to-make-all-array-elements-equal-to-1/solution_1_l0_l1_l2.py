class Solution:

    def minOperations(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        v2_214 = 0
        v3_125 = 0
        for v4_859 in nums:
            if v4_859 == 1:
                v2_214 = v2_214 + 1
            v3_125 = v5_381(v3_125, v4_859)
        if v2_214 > 0:
            return v1_754 - v2_214
        if v3_125 > 1:
            return -1
        v6_350 = v1_754
        for v7_328 in range(v1_754):
            v3_125 = 0
            for v8_242 in range(v7_328, v1_754):
                v3_125 = v5_381(v3_125, nums[v8_242])
                if v3_125 == 1:
                    v6_350 = min(v6_350, v8_242 - v7_328 + 1)
                    break
        return v6_350 + v1_754 - 2