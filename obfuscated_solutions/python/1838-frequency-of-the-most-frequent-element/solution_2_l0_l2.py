class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        curr = 0
        for right in range(len(nums)):
            target = nums[right]
            curr = curr + target
            if (right - left + 1) * target - curr > k:
                curr = curr - nums[left]
                left = left + 1
        return len(nums) - left