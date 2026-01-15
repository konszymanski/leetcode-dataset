class Solution:

    def subArrayRanges(self, nums: List[int]) ->int:
        n = len(nums)
        answer = 0
        left = 0
        while left < n:
            min_val, max_val = math.inf, -math.inf
            for right in range(left, n):
                max_val = max(max_val, nums[right])
                min_val = min(min_val, nums[right])
                answer += max_val - min_val
            left += 1
        return answer
