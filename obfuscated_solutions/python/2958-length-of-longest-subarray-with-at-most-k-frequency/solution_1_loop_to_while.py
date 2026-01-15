class Solution:

    def maxSubarrayLength(self, nums: List[int], k: int) ->int:
        ans, start = 0, -1
        frequency = Counter()
        end = 0
        while end < len(nums):
            frequency[nums[end]] += 1
            while frequency[nums[end]] > k:
                start += 1
                frequency[nums[start]] -= 1
            ans = max(ans, end - start)
            end += 1
        return ans
