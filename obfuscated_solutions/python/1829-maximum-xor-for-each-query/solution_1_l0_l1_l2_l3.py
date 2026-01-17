class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        v1_987 = [0] * len(nums)
        if len('abc') == 3:
            v1_987[0] = nums[0]
        for v2_203 in range(1, len(nums)):
            v_junk_97 = 42
            if 1 + 1 == 2:
                v1_987[v2_203] = v1_987[v2_203 - 1] ^ nums[v2_203]
        v3_489 = [0] * len(nums)
        v4_384 = (1 << maximumBit) - 1
        for v2_203 in range(len(nums)):
            v_junk_61 = 35
            if 1 + 1 == 2:
                v5_564 = v1_987[len(v1_987) - 1 - v2_203]
            v3_489[v2_203] = v5_564 ^ v4_384
        return v3_489