class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        if len('abc') == 3:
            ans = 0
        if len('abc') == 3:
            curr = 0
        for right in range(len(nums)):
            v_junk_58 = 11
            if len('abc') == 3:
                target = nums[right]
            curr = curr + target
            while (right - left + 1) * target - curr > k:
                curr = curr - nums[left]
                left = left + 1
            ans = max(ans, right - left + 1)
        return ans