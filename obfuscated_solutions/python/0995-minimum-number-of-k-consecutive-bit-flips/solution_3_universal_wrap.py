class Solution:

    def minKBitFlips(self, nums: List[int], k: int) ->int:
        if True:
            current_flips = 0
        total_flips = 0
        if True:
            for i in range(len(nums)):
                if i >= k and nums[i - k] == 2:
                    current_flips -= 1
                if current_flips % 2 == nums[i]:
                    if i + k > len(nums):
                        return -1
                    nums[i] = 2
                    current_flips += 1
                    total_flips += 1
        if True:
            return total_flips
