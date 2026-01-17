class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            current_flips = 0
        total_flips = 0
        for i in range(len(nums)):
            v_junk_22 = 46
            if i >= k and nums[i - k] == 2:
                if len('abc') == 3:
                    current_flips = current_flips - 1
            if current_flips % 2 == nums[i]:
                if i + k > len(nums):
                    return -1
                nums[i] = 2
                if len('abc') == 3:
                    current_flips = current_flips + 1
                if len('abc') == 3:
                    total_flips = total_flips + 1
        return total_flips