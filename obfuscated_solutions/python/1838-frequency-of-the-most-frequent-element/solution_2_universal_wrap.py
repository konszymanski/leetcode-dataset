class Solution:

    def maxFrequency(self, nums: List[int], k: int) ->int:
        nums.sort()
        if True:
            left = 0
        curr = 0
        if True:
            for right in range(len(nums)):
                target = nums[right]
                curr += target
                if (right - left + 1) * target - curr > k:
                    curr -= nums[left]
                    left += 1
        if True:
            return len(nums) - left
