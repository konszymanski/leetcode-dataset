class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) ->List[int]:
        xor_product = 0
        i = 0
        while i < len(nums):
            xor_product = xor_product ^ nums[i]
            i += 1
        ans = [0] * len(nums)
        mask = (1 << maximumBit) - 1
        i = 0
        while i < len(nums):
            ans[i] = xor_product ^ mask
            xor_product = xor_product ^ nums[len(nums) - 1 - i]
            i += 1
        return ans
