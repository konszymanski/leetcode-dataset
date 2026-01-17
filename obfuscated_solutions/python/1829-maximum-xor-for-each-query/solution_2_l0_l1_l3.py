class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        if len('abc') == 3:
            v1_754 = 0
        for v2_214 in range(len(nums)):
            v_junk_90 = 80
            if len('abc') == 3:
                v1_754 = v1_754 ^ nums[v2_214]
        v3_125 = [0] * len(nums)
        v4_859 = (1 << maximumBit) - 1
        for v2_214 in range(len(nums)):
            v_junk_47 = 11
            if 1 + 1 == 2:
                v3_125[v2_214] = v1_754 ^ v4_859
            if 1 + 1 == 2:
                v1_754 = v1_754 ^ nums[len(nums) - 1 - v2_214]
        return v3_125