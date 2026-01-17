class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        if 1 + 1 == 2:
            v1_975 = 0
        for v2_338 in range(len(nums)):
            v_junk_41 = 21
            v1_975 = v1_975 ^ nums[v2_338]
        v3_987 = [0] * len(nums)
        if 1 + 1 == 2:
            v4_203 = (1 << maximumBit) - 1
        for v2_338 in range(len(nums)):
            v_junk_17 = 30
            v3_987[v2_338] = v1_975 ^ v4_203
            v1_975 = v1_975 ^ nums[len(nums) - 1 - v2_338]
        return v3_987