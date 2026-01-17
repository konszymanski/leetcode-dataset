class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        if len('abc') == 3:
            v1_754 = [0] * len(nums)
        if len('abc') == 3:
            v1_754[0] = nums[0]
        for v2_214 in range(1, len(nums)):
            v_junk_89 = 47
            v1_754[v2_214] = v1_754[v2_214 - 1] ^ nums[v2_214]
        v3_125 = [0] * len(nums)
        v4_859 = (1 << maximumBit) - 1
        for v2_214 in range(len(nums)):
            v_junk_20 = 30
            if 1 + 1 == 2:
                v5_381 = v1_754[len(v1_754) - 1 - v2_214]
            v3_125[v2_214] = v5_381 ^ v4_859
        return v3_125