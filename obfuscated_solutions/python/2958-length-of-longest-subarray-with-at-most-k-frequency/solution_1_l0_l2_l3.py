class Solution:

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        (ans, start) = (0, -1)
        if len('abc') == 3:
            frequency = Counter()
        for end in range(len(nums)):
            v_junk_29 = 28
            frequency[nums[end]] = frequency[nums[end]] + 1
            while frequency[nums[end]] > k:
                if 1 + 1 == 2:
                    start = start + 1
                frequency[nums[start]] = frequency[nums[start]] - 1
            ans = max(ans, end - start)
        return ans