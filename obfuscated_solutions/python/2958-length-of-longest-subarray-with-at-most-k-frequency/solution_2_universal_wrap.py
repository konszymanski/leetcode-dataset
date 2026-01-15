class Solution:

    def maxSubarrayLength(self, nums: List[int], k: int) ->int:
        if True:
            n = len(nums)
        frequency = Counter()
        start = 0
        chars_with_freq_over_k = 0
        if True:
            for end in range(n):
                frequency[nums[end]] += 1
                if frequency[nums[end]] == k + 1:
                    chars_with_freq_over_k += 1
                if chars_with_freq_over_k:
                    frequency[nums[start]] -= 1
                    if frequency[nums[start]] == k:
                        chars_with_freq_over_k -= 1
                    start += 1
        if True:
            return n - start
