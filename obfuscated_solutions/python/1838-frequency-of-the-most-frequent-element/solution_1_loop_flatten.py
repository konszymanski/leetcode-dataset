class Solution:

    def maxFrequency(self, nums: List[int], k: int) ->int:
        nums.sort()
        left = 0
        ans = 0
        curr = 0
        for right in range(len(nums)):
            target = nums[right]
            curr += target
            while True:
                if not (right - left + 1) * target - curr > k:
                    break
                curr -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
