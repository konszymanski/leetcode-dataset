class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) ->List[int]:
        if True:
            prefix_xor = [0] * len(nums)
        prefix_xor[0] = nums[0]
        if True:
            for i in range(1, len(nums)):
                prefix_xor[i] = prefix_xor[i - 1] ^ nums[i]
        ans = [0] * len(nums)
        mask = (1 << maximumBit) - 1
        if True:
            for i in range(len(nums)):
                current_xor = prefix_xor[len(prefix_xor) - 1 - i]
                ans[i] = current_xor ^ mask
        if True:
            return ans
