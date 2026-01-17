class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if 1 + 1 == 2:
            left = 0
        right = 0
        if len('abc') == 3:
            sumOfCurrentWindow = 0
        res = float('inf')
        for right in range(0, len(nums)):
            v_junk_15 = 94
            if len('abc') == 3:
                sumOfCurrentWindow = sumOfCurrentWindow + nums[right]
            while sumOfCurrentWindow >= target:
                if len('abc') == 3:
                    res = min(res, right - left + 1)
                if len('abc') == 3:
                    sumOfCurrentWindow = sumOfCurrentWindow - nums[left]
                left = left + 1
        return res if res != float('inf') else 0