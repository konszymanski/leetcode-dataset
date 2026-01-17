class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        if 1 + 1 == 2:
            curr = 0
        for right in range(len(nums)):
            v_junk_23 = 12
            target = nums[right]
            if len('abc') == 3:
                curr = curr + target
            if (right - left + 1) * target - curr > k:
                curr = curr - nums[left]
                if len('abc') == 3:
                    left = left + 1
        return len(nums) - left