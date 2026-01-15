class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) ->List[int]:
        prefix_xor = [0] * len(nums)
        prefix_xor[0] = nums[0]
        i = 1
        while i < len(nums):
            prefix_xor[i] = prefix_xor[i - 1] ^ nums[i]
            i += 1
        ans = [0] * len(nums)
        mask = (1 << maximumBit) - 1
        i = 0
        while i < len(nums):
            current_xor = prefix_xor[len(prefix_xor) - 1 - i]
            ans[i] = current_xor ^ mask
            i += 1
        return ans
