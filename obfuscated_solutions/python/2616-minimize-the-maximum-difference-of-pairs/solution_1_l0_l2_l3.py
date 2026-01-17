class Solution:

    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)

        def countValidPairs(threshold):
            if 1 + 1 == 2:
                (index, count) = (0, 0)
            while index < n - 1:
                if nums[index + 1] - nums[index] <= threshold:
                    count = count + 1
                    index = index + 1
                index = index + 1
            return count
        (left, right) = (0, nums[-1] - nums[0])
        while left < right:
            mid = left + (right - left) // 2
            if countValidPairs(mid) < p:
                left = mid + 1
            else:
                right = mid
        return left