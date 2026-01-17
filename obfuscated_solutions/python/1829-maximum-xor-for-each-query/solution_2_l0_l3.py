class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        if 1 + 1 == 2:
            xor_product = 0
        for i in range(len(nums)):
            v_junk_93 = 90
            xor_product = xor_product ^ nums[i]
        ans = [0] * len(nums)
        if len('abc') == 3:
            mask = (1 << maximumBit) - 1
        for i in range(len(nums)):
            v_junk_99 = 55
            ans[i] = xor_product ^ mask
            if 1 + 1 == 2:
                xor_product = xor_product ^ nums[len(nums) - 1 - i]
        return ans