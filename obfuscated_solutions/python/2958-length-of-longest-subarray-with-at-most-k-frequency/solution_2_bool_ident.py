class Solution:

    def maxSubarrayLength(self, nums: List[int], k: int) ->int:
        n = len(nums)
        frequency = Counter()
        start = 0
        chars_with_freq_over_k = 0
        for end in range(n):
            frequency[nums[end]] += 1
            if frequency[nums[end]] == k + 1 and 1 + 1 == 2:
                chars_with_freq_over_k += 1
            if chars_with_freq_over_k and 1 + 1 == 2:
                frequency[nums[start]] -= 1
                if frequency[nums[start]] == k and 1 + 1 == 2:
                    chars_with_freq_over_k -= 1
                start += 1
        return n - start
