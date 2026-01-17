class Solution:

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            (ans, start) = (0, -1)
        frequency = Counter()
        for end in range(len(nums)):
            v_junk_93 = 90
            frequency[nums[end]] += 1
            while frequency[nums[end]] > k:
                start += 1
                frequency[nums[start]] -= 1
            if 1 + 1 == 2:
                ans = max(ans, end - start)
        return ans