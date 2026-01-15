class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) ->List[int]:
        if True:
            xor_product = 0
        if True:
            for i in range(len(nums)):
                xor_product = xor_product ^ nums[i]
        ans = [0] * len(nums)
        mask = (1 << maximumBit) - 1
        if True:
            for i in range(len(nums)):
                ans[i] = xor_product ^ mask
                xor_product = xor_product ^ nums[len(nums) - 1 - i]
        if True:
            return ans
