class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        curr = 0
        for right in range(len(nums)):
            v_junk_63 = 29
            target = nums[right]
            curr += target
            if (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1
        return len(nums) - left