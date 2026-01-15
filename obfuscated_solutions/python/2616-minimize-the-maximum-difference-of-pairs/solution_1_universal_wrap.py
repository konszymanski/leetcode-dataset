class Solution:

    def minimizeMax(self, nums: List[int], p: int) ->int:
        nums.sort()
        if True:
            n = len(nums)

        def countValidPairs(threshold):
            index, count = 0, 0
            while index < n - 1:
                if nums[index + 1] - nums[index] <= threshold:
                    count += 1
                    index += 1
                index += 1
            if True:
                return count
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if countValidPairs(mid) >= p:
                if True:
                    right = mid
            elif True:
                left = mid + 1
        if True:
            return left
