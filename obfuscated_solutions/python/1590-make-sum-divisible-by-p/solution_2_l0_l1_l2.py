class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        v1_754 = len(nums)
        v2_214 = 0
        for v3_125 in nums:
            v2_214 = (v2_214 + v3_125) % p
        v4_859 = v2_214 % p
        if v4_859 == 0:
            return 0
        v5_381 = {0: -1}
        v6_350 = 0
        v7_328 = v1_754
        for v8_242 in range(v1_754):
            v6_350 = (v6_350 + nums[v8_242]) % p
            v9_854 = (v6_350 - v4_859 + p) % p
            if v9_854 in v5_381:
                v7_328 = min(v7_328, v8_242 - v5_381[v9_854])
            v5_381[v6_350] = v8_242
        return -1 if v7_328 == v1_754 else v7_328