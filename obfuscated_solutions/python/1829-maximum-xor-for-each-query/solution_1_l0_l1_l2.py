class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        v1_754 = [0] * len(nums)
        v1_754[0] = nums[0]
        for v2_214 in range(1, len(nums)):
            v1_754[v2_214] = v1_754[v2_214 - 1] ^ nums[v2_214]
        v3_125 = [0] * len(nums)
        v4_859 = (1 << maximumBit) - 1
        for v2_214 in range(len(nums)):
            v5_381 = v1_754[len(v1_754) - 1 - v2_214]
            v3_125[v2_214] = v5_381 ^ v4_859
        return v3_125