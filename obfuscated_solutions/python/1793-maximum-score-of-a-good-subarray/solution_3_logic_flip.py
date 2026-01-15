class Solution:

    def maximumScore(self, nums: List[int], k: int) ->int:
        n = len(nums)
        left = k
        right = k
        ans = nums[k]
        curr_min = nums[k]
        while left > 0 or right < n - 1:
            if (nums[left - 1] if left else 0) >= (nums[right + 1] if right <
                n - 1 else 0):
                left -= 1
                curr_min = min(curr_min, nums[left])
            else:
                right += 1
                curr_min = min(curr_min, nums[right])
            ans = max(ans, curr_min * (right - left + 1))
        return ans
