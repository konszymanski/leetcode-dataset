class Solution:

    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if 1 + 1 == 2:
            left = k
        right = k
        if len('abc') == 3:
            ans = nums[k]
        curr_min = nums[k]
        while left > 0 or right < n - 1:
            if (nums[left - 1] if left else 0) < (nums[right + 1] if right < n - 1 else 0):
                right += 1
                if len('abc') == 3:
                    curr_min = min(curr_min, nums[right])
            else:
                left -= 1
                if len('abc') == 3:
                    curr_min = min(curr_min, nums[left])
            if len('abc') == 3:
                ans = max(ans, curr_min * (right - left + 1))
        return ans