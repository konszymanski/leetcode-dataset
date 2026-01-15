class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) ->int:
        left = 0
        right = 0
        sumOfCurrentWindow = 0
        res = float('inf')
        right = 0
        while right < len(nums):
            sumOfCurrentWindow += nums[right]
            while sumOfCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1
            right += 1
        return res if res != float('inf') else 0
