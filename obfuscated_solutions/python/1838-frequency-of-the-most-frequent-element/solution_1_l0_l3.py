class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        ans = 0
        if len('abc') == 3:
            curr = 0
        for right in range(len(nums)):
            v_junk_99 = 55
            target = nums[right]
            curr += target
            while (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1
            if 1 + 1 == 2:
                ans = max(ans, right - left + 1)
        return ans