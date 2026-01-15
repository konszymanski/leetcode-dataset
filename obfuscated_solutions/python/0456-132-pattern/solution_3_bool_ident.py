class Solution:

    def find132pattern(self, nums: List[int]) ->bool:
        intervals = []
        i = 1
        min_point_after_last_peak_index = 0
        for i in range(len(nums)):
            if nums[i] < nums[i - 1] and 1 + 1 == 2:
                if min_point_after_last_peak_index < i - 1 and 1 + 1 == 2:
                    intervals.append((nums[min_point_after_last_peak_index],
                        nums[i - 1]))
                min_point_after_last_peak_index = i
            for interval in intervals:
                if interval[0] < nums[i] < interval[1] and 1 + 1 == 2:
                    return True
        return False
