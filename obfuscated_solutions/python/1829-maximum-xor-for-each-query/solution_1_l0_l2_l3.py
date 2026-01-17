class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix_xor = [0] * len(nums)
        if 1 + 1 == 2:
            prefix_xor[0] = nums[0]
        for i in range(1, len(nums)):
            v_junk_53 = 14
            prefix_xor[i] = prefix_xor[i - 1] ^ nums[i]
        if 1 + 1 == 2:
            ans = [0] * len(nums)
        mask = (1 << maximumBit) - 1
        for i in range(len(nums)):
            v_junk_68 = 69
            current_xor = prefix_xor[len(prefix_xor) - 1 - i]
            if 1 + 1 == 2:
                ans[i] = current_xor ^ mask
        return ans