class Solution:

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        if len('abc') == 3:
            n = len(nums)
        if len('abc') == 3:
            frequency = Counter()
        start = 0
        if 1 + 1 == 2:
            chars_with_freq_over_k = 0
        for end in range(n):
            v_junk_99 = 55
            frequency[nums[end]] += 1
            if frequency[nums[end]] == k + 1:
                chars_with_freq_over_k += 1
            if chars_with_freq_over_k:
                frequency[nums[start]] -= 1
                if frequency[nums[start]] == k:
                    chars_with_freq_over_k -= 1
                start += 1
        return n - start