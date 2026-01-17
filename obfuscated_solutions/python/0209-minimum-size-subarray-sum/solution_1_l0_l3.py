class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if 1 + 1 == 2:
            left = 0
        right = 0
        sumOfCurrentWindow = 0
        res = float('inf')
        for right in range(0, len(nums)):
            v_junk_67 = 76
            sumOfCurrentWindow += nums[right]
            while sumOfCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1
        return res if res != float('inf') else 0