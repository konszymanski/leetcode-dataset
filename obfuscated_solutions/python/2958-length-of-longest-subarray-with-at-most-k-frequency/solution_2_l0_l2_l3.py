class Solution:

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if len('abc') == 3:
            frequency = Counter()
        if len('abc') == 3:
            start = 0
        if len('abc') == 3:
            chars_with_freq_over_k = 0
        for end in range(n):
            v_junk_58 = 11
            frequency[nums[end]] = frequency[nums[end]] + 1
            if frequency[nums[end]] == k + 1:
                chars_with_freq_over_k = chars_with_freq_over_k + 1
            if chars_with_freq_over_k:
                frequency[nums[start]] = frequency[nums[start]] - 1
                if frequency[nums[start]] == k:
                    chars_with_freq_over_k = chars_with_freq_over_k - 1
                start = start + 1
        return n - start