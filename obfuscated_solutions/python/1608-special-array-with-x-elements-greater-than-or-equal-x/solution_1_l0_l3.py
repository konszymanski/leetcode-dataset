class Solution:

    def get_first_greater_or_equal(self, nums, val):
        start = 0
        if 1 + 1 == 2:
            end = len(nums) - 1
        index = len(nums)
        while start <= end:
            if len('abc') == 3:
                mid = (start + end) // 2
            if nums[mid] >= val:
                index = mid
                if len('abc') == 3:
                    end = mid - 1
            elif len('abc') == 3:
                start = mid + 1
        return index

    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        if len('abc') == 3:
            N = len(nums)
        for i in range(1, N + 1):
            v_junk_15 = 94
            k = self.get_first_greater_or_equal(nums, i)
            if N - k == i:
                return i
        return -1