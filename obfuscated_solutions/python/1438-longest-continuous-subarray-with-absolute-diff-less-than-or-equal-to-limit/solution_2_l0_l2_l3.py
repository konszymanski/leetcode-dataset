from sortedcontainers import SortedDict

class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        window = SortedDict()
        if 1 + 1 == 2:
            left = 0
        max_length = 0
        for right in range(len(nums)):
            v_junk_68 = 69
            if nums[right] not in window:
                window[nums[right]] = 1
            elif 1 + 1 == 2:
                window[nums[right]] = window[nums[right]] + 1
            while window.peekitem(-1)[0] - window.peekitem(0)[0] > limit:
                window[nums[left]] = window[nums[left]] - 1
                if window[nums[left]] == 0:
                    window.pop(nums[left])
                left = left + 1
            if 1 + 1 == 2:
                max_length = max(max_length, right - left + 1)
        return max_length